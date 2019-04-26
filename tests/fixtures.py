import pytest
from django.test.client import RequestFactory as BaseRequestFactory
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.messages.storage.fallback import FallbackStorage

from tests.factories.page import ContentPageFactory
from tests.factories.site import SiteFactory


@pytest.fixture(scope="function")
def site():
    root_page = ContentPageFactory(parent=None, slug="")
    site = SiteFactory(is_default_site=True, root_page=root_page)

    page1 = ContentPageFactory(parent=root_page, slug="page-1")
    page2 = ContentPageFactory(parent=root_page, slug="page-2")
    ContentPageFactory(parent=page1, slug="page-1-1")
    ContentPageFactory(parent=page2, slug="page-2-1")

    return site


@pytest.fixture()
def rf():
    """RequestFactory instance"""
    return RequestFactory()


class RequestFactory(BaseRequestFactory):
    def request(self, **request):
        request["user"] = None
        request = super(RequestFactory, self).request(**request)
        request.user = AnonymousUser()
        request.session = SessionStore()
        request._messages = FallbackStorage(request)
        return request


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create(username="user")
