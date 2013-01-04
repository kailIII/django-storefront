#!/usr/bin/env python
from setuptools import setup, find_packages

import storefront

setup(name='storefront',
    version=storefront.__version__,
    description='A clear and powerfull e-commerce app powered with Django',
    long_description='A clear and powerfull e-commerce app powered with Django',
    keywords='django, store, storefront, sales',
    author=storefront.__author__,
    author_email=storefront.__email__,
    url=storefront.__url__,

    packages=find_packages(exclude=['tests']),

    classifiers = [
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Office/Business',
    ],

    license=storefront.__license__,
    include_package_data=True,
    zip_safe=False,
)
