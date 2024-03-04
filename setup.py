from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="scp", 
    version="0.1",
    description="A deep generative model for single-cell proteomics",
    packages=find_packages(),
    install_requires=requirements,
)
