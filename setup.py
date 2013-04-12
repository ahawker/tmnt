__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'

import tmnt

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=tmnt.__name__,
    version=tmnt.__version__,
    description='Python module for mutation testing.',
    long_description=open('README.md').read(),
    author='Andrew Hawker',
    author_email='andrew.r.hawker@gmail.com',
    url='https://github.com/ahawker/tmnt',
    license=open('LICENSE.md').read(),
    package_dir={'tmnt': 'tmnt'},
    packages=['tmnt'],
    test_suite='tests',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    )
)
