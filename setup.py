from distutils.core import setup

import thorlabs_kinesis as thk

setup(
    name="thorlabs-kinesis",
    version=thk.__version__,
    description="Python bindings to Thorlabs Kinesis API.",
    author="Ertugrul Karademir",
    euthor_email="ekarademir@gmail.com",
    url="https://github.com/ekarademir/thorlabs-kinesis",
    packages=["thorlabs-kinesis", "thorlabs-kinesis.ext"]
)