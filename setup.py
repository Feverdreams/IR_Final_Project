# -*- coding:utf-8 -*-
# Author：hankcs
# Date: 2018-03-11 20:54
from os.path import abspath, join, dirname
from setuptools import find_packages, setup

setup(
    name='qa',
    version='0.0.1',
    description='QA',
    long_description=open(join(abspath(dirname(__file__)), 'README.md'), encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    keywords='nlp',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=['hanlp'],
)
