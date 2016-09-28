import os
import sys
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='habitica-challenge-wrangler',
    version='2.0.0',
    description='Habitica Challenge Data Wrangler - pick winners from challenge data',
    long_description=long_description,
    url='https://github.com/DC23/habitica-challenge-wrangler',
    license='Apache 2.0',

    # Author details
    author='JugglinDan',
    author_email='jugglindan@gmail.com',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',

        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment :: Role-Playing',
        'Topic :: Utilities',
    ],

    # What does your project relate to?
    keywords='Habitica, HabitRPG',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['tests']),

    include_package_data=True,

    platforms='any',

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=[
        'future',
        'pandas>=0.17.0',
        'xlwt',
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [
            'bumpversion',
        ],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # Delete either or both of these if not required (and remove the corresponding imports in the package __init__.py
    entry_points={
        'console_scripts': [
            'pick-winner = habitica_challenge_wrangler:pick_winner',
        ],
    },

    # Is your project zip safe?
    zip_safe=True,
)
