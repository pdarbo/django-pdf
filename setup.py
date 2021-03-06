#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = __import__('pdf').__version__


setup(name='django-pdf',
      version=VERSION,
      description='A Django app for managing and processing PDF documents.',
      author='Patrick Altman',
      author_email='paltman@gmail.com',
      url='http://github.com/paltman/django-pdf/',
      packages=find_packages(),
      classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data = True,
    zip_safe = False,
    install_requires = ['django', 'celery', 'boto', 'simplejson', 'ghettoq']
)