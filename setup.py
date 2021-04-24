#!/usr/bin/env python3

"""
The AES-Toolbox setup script.
Run "python3 setup.py install"

$ python3 setup.py --help-commands
"""

from __future__ import print_function

from aestoolbox.release import __version__, __author__, __license__, __description__, __url__

import sys

try:
    from setuptools import setup, find_packages
except ModuleNotFoundError:
    print("Please install pip and python-setuptools.")
    sys.exit(-1)


with open("README.pypi.rst") as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = ["pytest-runner", "setuptools"]

test_requirements = [
    "pytest>=3",
]

setup(
    author=__author__,
    version=__version__,
    python_requires=">=3.8",
    scripts=["bin/aes-schedule"],
    classifiers=[
        "Intended Audience :: Developers",
        f"License :: OSI Approved :: {__license__}",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description=__description__,
    install_requires=requirements,
    license=__license__,
    long_description=readme + "\n\n",
    include_package_data=True,
    keywords="AES Key Schedule Rijndael AES-128 AES-192 AES-192 AES Key \
    Expansion aeskeyschedule aes toolbox aes-key",
    name="aestoolbox",
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url=__url__,
    zip_safe=False,
)
