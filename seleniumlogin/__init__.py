from importlib import import_module
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY


def force_login(user, driver, base_url):
    from django.conf import settings
    SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
    selenium_login_start_page = getattr(settings, 'SELENIUM_LOGIN_START_PAGE', '/page_404/')
    driver.get('{}{}'.format(base_url, selenium_login_start_page))

    session = SessionStore()
    session[SESSION_KEY] = user.id
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session[HASH_SESSION_KEY] = user.get_session_auth_hash()
    session.save()

    cookie = {
        'name': settings.SESSION_COOKIE_NAME,
        'value': session.session_key,
        'path': '/'
    }

    driver.add_cookie(cookie)
    driver.refresh()
