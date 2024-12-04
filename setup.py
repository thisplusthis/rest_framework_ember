#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def get_readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='rest_framework_ember',
    version='1.0.4',
    description="Working version of rest_framework_ember for Django 4.x+",
    long_description=get_readme(),
    author="james mcdonald",
    author_email='thisplusthis@gmail.com',
    url='https://github.com/thisplusthis/rest_framework_ember',
    license='BSD',
    keywords="",
    packages=find_packages(),
    install_requires=['django', 'djangorestframework', 'inflection'],
    platforms=['any'],
    classifiers=[]
)

