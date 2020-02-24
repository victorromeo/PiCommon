from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup (
    name='picommon',
    version='0.1.0',
    description='Shell and python utility functions for Raspberry Pi management',
    long_description=readme,
    author='victorromeo',
    author_email='',
    url='https://github.com/victorromeo/PiCommon',
    license=license,
    packages=find_packages(exclude=('doc', 'tests'))
)