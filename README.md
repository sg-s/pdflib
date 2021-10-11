# pdflib.make

Pretty printing of PDFs from Jupyter notebooks

## Installation

Assuming you are going to use pdflib in a project that you want to make installable, add the following to your `setup.py`:


```python

from setuptools import setup

setup(
    ...
    install_requires=[
   		...
        'pdflib @ git+https://github.com/sg-s/pdflib.git',
    ],
	...
)
```



## Usage

At the bottom of a Jupyter notebook, add the following:

```python
pdflib.make("/full/path/to/your/notebook.ipynb")

```

## License

GPL v3