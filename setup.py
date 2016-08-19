#!/usr/bin/env python3
from setuptools import setup

README = open("README.rst").read()

CLASSIFIERS = """\
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
""".splitlines()

setup(
    name="aioconsole",
    version="0.1.0",
    packages=["aioconsole"],
    entry_points={'console_scripts': ['apython = aioconsole:run_apython']},

    license="GPLv3",
    classifiers=CLASSIFIERS,
    description="Asynchronous python console and interfaces",
    long_description=README,

    author="Vincent Michel",
    author_email="vxgmichel@gmail.com",
    url='https://github.com/vxgmichel/aioconsole',
    download_url='http://pypi.python.org/pypi/aioconsole',
)
