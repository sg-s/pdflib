# pdflib.make

Pretty printing of PDFs from Jupyter notebooks


This aims to do in python what [pdflib.make](https://github.com/sg-s/srinivas.gs_mtools/blob/master/src/%2Bpdflib/make.m) does in MATLAB. 

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

Make sure you import this using:

```python
from pdflib import pdflib
```

At the bottom of a Jupyter notebook, add the following:

```python
pdflib.make("/full/path/to/your/notebook.ipynb")

```


## Comparison of MATLAB and python versions

| MATLAB | python |
| ------- | ------ |
| uses [publish](https://www.mathworks.com/help/matlab/ref/publish.html) as a backend |  uses `jupyter nbconvert`|
| Starts from pure text files | Starts from binary jupyter notebooks |
| sophisticated git support; all dependencies are versioned | TODO |
| entire script re-run on publish | no computations performed on publish | 


## License

GPL v3