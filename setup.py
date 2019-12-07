#!/usr/bin/env python

from setuptools import setup
from chargeamps import __version__

setup(
    name='chargeamps',
    version=__version__,
    description='Charge-Amps API bindings for Python',
    author='Jakob Schlyter',
    author_email='jakob@kirei.se',
    license='BSD',
    keywords='ev',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    url='https://github.com/kirei/python-chargeamps',
    python_requires=">=3.6.1",
    packages=['chargeamps'],
    install_requires=[
        'aiohttp',
        'asyncio',
        'dataclasses',
        'dataclasses-json',
        'isodate',
        'marshmallow',
        'pyjwt',
        'setuptools',
    ],
    entry_points={
        "console_scripts": [
            "chargeamps = chargeamps.cli:main"
        ]
    }
)
