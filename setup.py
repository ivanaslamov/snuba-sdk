#!/usr/bin/env python

"""
Snuba-SDK - SnQL SDK for Snuba
=====================================

**Snuba-SDK is an SDK for Snuba.** Check out `GitHub
<https://github.com/getsentry/snuba-sdk>`_ to find out more.
"""

import os
from setuptools import setup, find_packages  # type: ignore

here = os.path.abspath(os.path.dirname(__file__))


def get_file_text(file_name: str) -> str:
    with open(os.path.join(here, file_name)) as in_file:
        return in_file.read()


setup(
    name="snuba-sdk",
    version="0.0.15",
    author="Sentry Team and Contributors",
    author_email="hello@sentry.io",
    url="https://github.com/getsentry/snuba-sdk",
    project_urls={
        "Changelog": "https://github.com/getsentry/snuba-sdk/blob/main/CHANGES.md",
    },
    description="Snuba SDK for generating SnQL queries.",
    long_description=get_file_text("README.rst"),
    long_description_content_type="text/x-rst",
    packages=find_packages(exclude=("tests", "tests.*")),
    # PEP 561
    package_data={"snuba_sdk": ["py.typed"]},
    zip_safe=False,
    license="BSD",
    install_requires=["dataclasses"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
