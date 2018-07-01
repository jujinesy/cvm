# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import machina

setup(
    name='django-machina',
    version=machina.__version__,
    author='Morgan Aubert',
    author_email='morgan.aubert@zoho.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ellmetha/django-machina',
    license='BSD',
    description='A Django forum engine for building powerful community driven websites.',
    keywords='django forum board messages',
    zip_safe=False,
    install_requires=[
        'django>=1.11',

        # Django-mptt is required to handle the tree hierarchy of nested forums
        'django-mptt>=0.8',

        # Machina uses Django-haystack to provide search support
        'django-haystack>=2.1',

        # Pillow is required for image fields
        'pillow>=2.2',

        # Machina uses Markdown by default as a syntax for forum messages ; but you can change this
        'markdown2>=2.3',

        # Machina's default templates use django-widget-tweaks to render form fields ; but you can
        # override this
        'django-widget-tweaks>=1.4',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    ],
)