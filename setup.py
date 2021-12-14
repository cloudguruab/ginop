from setuptools import setup, find_packages

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='ginop',
    version='1.0',
    description='A module for smart contract management of employee productivity workflows',
    license="MIT",
    long_description=long_description,
    author='Adrian Brown',
    author_email='Adrian Brown',
    url="https://usesource.app/",
    packages=find_packages(),
    install_requires=[]
)
