This is more of a personal reminder than an example. 
These are the scripts I use to upload to PyPI, so I will use them to update the package.
Feel free to use this as a little publishing reference :)

# Set up
This file must be present to continue. There is a lot in it, so just include all the following:
```py
from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'package_name',
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

# __init__.py
This is used to specify what is visible in the package. I put it in a foler with the same name as the package and specified this in `setup.py`. All scripts are in this folder. For this project, this file is very simple:
```py
from .model import load_model
```
This brings the load_model function to the package level.

# Building
First, build with wheel. You will have to increase the version number in `setup.py` to avoid conflicts.

Run the following script in the project terminal:
```
python setup.py sdist bdist_wheel
```

# Publishing
Use twine to upload to PyPI. Run the follwin script:
```
twine upload dist/*
```
You will need to give your information to actually upload the package. 