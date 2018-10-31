from setuptools import setup, find_packages

import thorlabs_kinesis as thk

setup(
    name="thorlabs_kinesis",
    version=thk.__version__,
    description="Python bindings to Thorlabs Kinesis API.",
    author="Ertugrul Karademir",
    author_email="ekarademir@gmail.com",
    url="https://github.com/ekarademir/thorlabs-kinesis",
    packages=find_packages()
)
