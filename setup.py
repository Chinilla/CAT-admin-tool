#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "chinilla-blockchain",
]

dev_dependencies = [
    "black",
]

setup(
    name="Chinilla_CAT_Admin",
    version="0.0.1",
    author="Edward Teach",
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": ["chcats = chcats.chcats:main"],
    },
    author_email="edward@chinilla.net",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/Chinilla",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Tools to administer issuance and redemption of a Chinilla Asset Token or CAT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/Chinilla/chinilla-CAT-admin",
        "Source": "https://github.com/Chinilla/chinilla-CAT-admin",
    },
)
