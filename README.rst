django-selenium-login: Quick Selenium login for Django
======================================================

django-selenium-login sets a session cookie for the Selenium driver and a creates a session object for the Django backend in order to force a user to quickly login.

Usage
-----
With django-selenium-login you can use the force_login function to force a user to qucikly login before using the the Selenium driver to proceeds on pages that requires login. The function takes a Django user, a Selenium driver, and the base url for the live server. Here is an example of how to use the force_login function in a test:

.. code-block:: python

    from seleniumlogin import force_login


    def test_use_django_selenium_login_to_force_login(selenium, live_server):
        User = get_user_model()
        user = User.objects.create_user(username='myuser', password='password')
        force_login(user, selenium, live_server.url)
        selenium.get('{}/a/url/which/requires/login/'.format(live_server.url))

Before setting the session cookie for the Selenium driver, the driver must access a page in the project. By default it will try to access the /page_404/ page. This can be changed by changing the SELENIUM_LOGIN_START_PAGE setting in the settings file for your tests. A blank page is used for the tests in this lib.

Installation
------------
Use pip to install django-selenium-login:

.. code-block:: shell

    pip install django-selenium-login

For developers
--------------
Create venv using:

.. code-block:: shell

    make venv

Run tests for multiple versions of Python and Django for a specific browser using tox:

.. code-block:: shell

    tox -- --driver=Chrome

Use environment variable SESSION_ENGINE to change authentication backend.

To run tests for all authentication backends for Chrome, Firefox, and PhantomJS:

.. code-block:: shell

    ./run_tests.sh
