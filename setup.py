#!/usr/bin/env python

from setuptools import setup, find_packages

tests_require = ["coverage", "flake8", "wheel", "pytest"]

setup(
    name="yq",
    version="2.6.0",
    url="https://github.com/kislyuk/yq",
    license="Apache Software License",
    author="Andrey Kislyuk",
    author_email="kislyuk@gmail.com",
    description="Command-line YAML/XML/TOML processor - jq wrapper for YAML/XML/TOML documents",
    long_description=open("README.rst").read(),
    install_requires=[
        "setuptools",
        "PyYAML >= 3.11",
        "xmltodict >= 0.11.0",
        "toml >= 0.9.4",
    ],
    tests_require=tests_require,
    extras_require={"test": tests_require},
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'yq=yq:main',
            'xq=yq:xq_cli',
            'tomlq=yq:tomlq_cli'
        ],
    },
    test_suite="test",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
