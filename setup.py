# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

version = '0.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = read('README.txt') + '\n' + read('js', 'ngupload',
        'test_ngupload.txt') + '\n' + read('CHANGES.txt')

setup(
    name='js.ngupload',
    version=version,
    description='Fanstatic packaging of ngUpload',
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['fanstatic', 'setuptools', 'js.angular'],
    entry_points={'fanstatic.libraries': ['ngupload = js.ngupload:library']},
    )
