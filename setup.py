
from setuptools import setup, find_packages
import sys, os

setup(name='kpick',
    version='0.1.0',
    description="Kingpick CLI client - computer vision tool",
    long_description="Kingpick CLI client - computer vision tool",
    classifiers=[],
    keywords='',
    author='D1',
    author_email='d1@ciandt.com',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        kpick = kpick.cli.main:main
    """,
    namespace_packages=[],
    )
