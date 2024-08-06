# PyObjLoader
An obj model loader for python. Currently will only return a numpy array of vertices containing position, uv, and normals.

## Setup
Run the install command

```pip
pip install pyobjloader
```

## Import
Import the load function

```py
from pyobjloader import load_model
```

## Use
To get the numpy array of vertices, first setup a directory containing the .obj

```
project
│ main.py
│ my_model_directory
└─── my_model.obj
```

Then pass the directory into the load function
```py
model = load_model('my_model_directory')
vertex_array = model.vertex_array
```

## Format
The format of the vertex array is as follows:

```py
# ModernGL Specifications
vertex_format = '3f 2f 3f'
vertex_attribs = ['in_position', 'in_texcoord', 'in_normal']
```

## Example with ModernGL
Here is an example VAO made with ModernGL and PyObjLoader

```py
# Make sure you have a context and shader program (see moderngl docs)
ctx = ...
program = ...

# Load the model using pyobjloader
model = load_model('my_model_directory')
vertex_array = model.vertex_array

# Make a vertex buffer object with the vertex data
vbo = ctx.buffer(vertex_data)

# VBO Formatting
vertex_format = '3f 2f 3f'
vertex_attribs = ['in_position', 'in_texcoord', 'in_normal']

# Create a vertex array object
vao = ctx.vertex_array(program, [(vbo, vertex_format, *vertex_attribs)])
```