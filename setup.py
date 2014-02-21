# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='django-reloj-poblacional',
    version='1.0',
    url='https://github.com/heraldmatias/django-reloj-poblacional',
    license='GPL v.3',
    description='App que implementa el algoritmo de reloj poblacional',

    long_description=read('README.md'),

    author='Herald Olivares',
    author_email='heraldmatias.oz@gmail.com',

    packages=find_packages(),

    install_requires=['setuptools', 'django'],

    classifiers=[
        'Development Status :: Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v.3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
