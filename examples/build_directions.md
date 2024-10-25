This is more of a personal reminder than an example. 
These are the scripts I use to upload to PyPI, so I will use them to update the package.
Feel free to use this as a little publishing reference :)

# Required Packages
Run the following command to get all the required packages:
```
pip install wheel setuptools twine
```

# Project Folder
The folder you are working in should look something like this:
```
project
│ setup.py
│ README.md
│ LICENSE.txt
│ package_name
|─── __init__.py
└─── package_script_1.py
```

# setup.py
This file must be present to continue. There is a lot in it, so just include all the following:
```py
from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'package_name',  # Name of folder containing scripts and __init__
    version = '0.0.1',
    url = 'github.com',
    author = 'Name',
    author_email = 'mail@gmail.com',
    description = 'Short description...',
    long_description = long_description,  # Load from file
    long_description_content_type = 'text/markdown',
    packages=find_packages(),
    install_requires=["numpy"],  # Include all used packages
)
```

# License and Readme
It is good practice to include both a license and readme file in your package. I typically use the MIT license. README should give an outline of the package.

# __init__.py
This is used to specify what is visible in the package. For most projects, this file is very simple:
```py
from .package_script_1 import my_function
```
This brings my_function to the package level.

# Building
First, build with wheel. If you have already published this package, you will have to increase the version number in `setup.py` to avoid conflicts when uploading to PyPI.

Run the following script in the project terminal:
```
python setup.py sdist bdist_wheel
```

# Publishing
Use twine to upload to PyPI. Run the following script:
```
twine upload dist/*
```
You will need to give your API key upload the package. 