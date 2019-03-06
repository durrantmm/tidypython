
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tidypython',
    version='0.0.1.dev3',
    description='A package designed to syntactically mimic the tidyr R package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/durrantmm/tidypython',
    author='Matt Durrant',
    author_email='matthewgeorgedurrant@gmail.com',
    keywords='tidyr R syntax',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required,
    install_requires = [
        'pandas',
        'dplython',
        'readpy'
    ]
)