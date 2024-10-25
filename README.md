# PyObjLoader
An obj model loader for python. Ideal for 3D data and graphics.

## Setup
Run the install command.

```pip
pip install pyobjloader
```

## Import
Import the load function

```py
from pyobjloader import load_model
```

## Use
To get the numpy array of vertices, first place the .obj somewhere in your project file (example shown)

```
project
│ main.py
│ my_model_directory
└─── my_model.obj
```

Then pass the file path into the load function
```py
model = load_model('my_model_directory/my_model.obj')
vertex_data = model.vertex_data
```
Examples for how to access more data from the model are in the github examples folder.

## Format
The format of the vertex data for an obj is stored in the model:

```py
# ModernGL Specifications
vertex_format = model.format  # ie. '3f 2f 3f'
vertex_attribs = model.attribs  # ie. ['in_position', 'in_uv', 'in_normal']
```

Possible attributes include `['in_position', 'in_uv', 'in_normal']` and `['in_position', 'in_normal']` (Normals are calculated if not given)

## Example with ModernGL
Here is an example VAO made with ModernGL and PyObjLoader

```py
# Make sure you have a context and shader program (see moderngl docs)
ctx = ...
program = ...

# Load the model using pyobjloader
model = load_model('my_model_directory/my_model')
vertex_data = model.vertex_data

# Make a vertex buffer object with the vertex data
vbo = ctx.buffer(vertex_data)

# Create a vertex array object
vao = ctx.vertex_data(program, [(vbo, model.format, *model.attribs)])
```

##