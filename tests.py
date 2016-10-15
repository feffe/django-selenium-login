import pytest
from django.contrib.auth import get_user_model

from seleniumlogin import force_login

pytestmark = [pytest.mark.django_db(transaction=True)]


def test_non_authenticated_user_cannot_access_test_page(selenium, live_server):
    selenium.get('{}/test/login_required/'.format(live_server.url))
    assert 'fail' in selenium.page_source


def test_authenticated_user_can_access_blank_login_page(selenium, live_server):
    User = get_user_model()
    user = User.objects.create_user(username='selenium', password='password')

    force_login(user, selenium, live_server.url)
    selenium.get('{}/test/login_required/'.format(live_server.url))
    assert 'success' in selenium.page_source
