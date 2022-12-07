#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "chinilla-blockchain==1.3.0",
]

dev_dependencies = [
    "black==21.12b0",
    "pytest",
    "pytest-env",
]

setup(
    name="chinilla_CAT_admin",
    version="1.1.0",
    author="Edward Teach",
    entry_points={
        "console_scripts": [
            "cats = cats.cats:main",
            "secure_the_bag = cats.secure_the_bag:main",
            "unwind_the_bag = cats.unwind_the_bag:main"
        ],
    },
    author_email="edward@chinilla.net",
    setup_requires=["setuptools_scm"],
    packages=['chcats'],
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
