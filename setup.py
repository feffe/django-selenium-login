import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-selenium-login",
    version="1.0.1",
    author="Fredrik Westermark",
    author_email="feffe.westermark@gmail.com",
    description=("A quick login for selenium tests to be used in Django projects"),
    license="MIT",
    keywords="selenium django login",
    url="https://github.com/feffe/django-selenium-login",
    packages=['seleniumlogin', 'test_'],
    install_requires=['django>=1.8'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Quality Assurance",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
