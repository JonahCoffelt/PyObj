"""
Example for loading a model from file
"""

from pyobjloader import load_model

# Load the model from file
model = load_model("examples/models/monkey.obj")

# Contains all data needed for a model buffer
vertex_data = model.vertex_data