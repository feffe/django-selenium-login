import pytest
from django.contrib.auth import get_user_model

from seleniumlogin import force_login
from test_.models import MyUser

pytestmark = [pytest.mark.django_db(transaction=True)]


@pytest.fixture
def base_url_(live_server, base_url):
    port = live_server.url.split(':')[-1]
    if base_url:
        return f'{base_url}:{port}'
    return f'http://127.0.0.1:{port}'


@pytest.mark.nondestructive
def test_non_authenticated_user_cannot_access_test_page(selenium, base_url_):
    selenium.get(f'{base_url_}/test/login_required/')
    assert 'fail' in selenium.page_source


@pytest.mark.nondestructive
def test_authenticated_user_can_access_test_page(selenium, base_url_):
    User = get_user_model()
    user = User.objects.create_user(username='selenium', password='password')
    force_login(user=user, driver=selenium, base_url=base_url_)
    selenium.get(f'{base_url_}/test/login_required/')
    assert 'success' in selenium.page_source


@pytest.mark.nondestructive
def test_authenticated_user_with_uuid_pk_field_can_access_test_page(settings, selenium, base_url_):
    settings.AUTH_USER_MODEL = 'test_.MyUser'
    user = MyUser.objects.create_user(username='selenium', password='password')
    force_login(user=user, driver=selenium, base_url=base_url_)
    selenium.get(f'{base_url_}/test/login_required/')
    assert 'success' in selenium.page_source
