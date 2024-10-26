"""
Often, it is helpful to get the tangent and bitangents of models.
The most common use of this in graphics is for normal mapping.
This example shows how to access and manage model tangent data.
"""

from pyobjloader import load_model
import numpy as np

# Load the model from file. Must the calculate_tangents flag to True. 
model = load_model("examples/models/monkey.obj", calculate_tangents=True)

# Contains all data needed for a model buffer
vertex_data = model.vertex_data
# Contains additional tangent and bitangent data
tangent_data = model.tangent_data

# Combine data into a single buffer
combined_data = np.hstack([vertex_data, tangent_data])