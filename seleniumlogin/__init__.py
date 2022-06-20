from importlib import import_module
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY


def force_login(user, driver, base_url):
    from django.conf import settings

    # port from https://github.com/django/django/commit/47744a0a4ed0b9e2d3f52de65abcf6cef9a14e31
    def get_backend():
        from django.contrib.auth import load_backend
        for backend_path in settings.AUTHENTICATION_BACKENDS:
            backend = load_backend(backend_path)
            if hasattr(backend, 'get_user'):
                return backend_path

    SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
    selenium_login_start_page = getattr(settings, 'SELENIUM_LOGIN_START_PAGE', '/page_404/')
    driver.get('{}{}'.format(base_url, selenium_login_start_page))

    session = SessionStore()
    session[SESSION_KEY] = user._meta.pk.value_to_string(user)
    session[BACKEND_SESSION_KEY] = get_backend()
    session[HASH_SESSION_KEY] = user.get_session_auth_hash()
    session.save()

    cookie = {
        'name': settings.SESSION_COOKIE_NAME,
        'value': session.session_key,
        'path': '/'
    }
    driver.add_cookie(cookie)
    driver.refresh()
