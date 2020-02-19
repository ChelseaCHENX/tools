#!/usr/bin/env python

from setuptools import setup, find_packages
import subprocess
import sys

version = '1.9dev'

# Try to append the git hash if we can
if 'dev' in version:
    try:
        git_hash = str(subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()).strip('"\'').lstrip("b'")
        version = '{}-{}'.format(version, git_hash)
    except IndexError:
        pass

with open('README.md') as f:
    readme = f.read()

setup(
    name = 'nf-core',
    version = version,
    description = 'Helper tools for use with nf-core Nextflow pipelines.',
    long_description = readme,
    long_description_content_type='text/markdown',
    keywords = ['nf-core', 'nextflow', 'bioinformatics', 'workflow', 'pipeline', 'biology', 'sequencing', 'NGS', 'next generation sequencing'],
    author = 'Phil Ewels',
    author_email = 'phil.ewels@scilifelab.se',
    url = 'https://github.com/nf-core/tools',
    license = 'MIT',
    scripts = ['scripts/nf-core'],
    install_requires = [
        'cookiecutter',
        'click',
        'GitPython',
        'jsonschema',
        'pyyaml',
        'requests',
        'requests_cache',
        'tabulate'
    ],
    setup_requires=[
        'twine>=1.11.0',
        'setuptools>=38.6.'
    ],
    packages = find_packages(exclude=('docs')),
    include_package_data = True,
    zip_safe = False
)
