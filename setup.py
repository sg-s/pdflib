"""
setup file

Run "pip install ." to install this
"""


from setuptools import find_packages, setup

setup(
    name='pdflib',
    version='21.11.3',
    packages=find_packages(exclude=('tests', 'docs')),
    description='Automatic pretty printing of PDFs from Jupyter notebooks',
    url='URL',
    author='Srinivas Gorur-Shandilya',
    author_email='code@srinivas.gs',
)
