"""
Example for how to use the model point_indices attribute to get vertex positions
"""

from pyobjloader import load_model
import numpy as np

# Load the model from file
model = load_model("examples/models/monkey.obj")

# Get just the positions from vertex data
points_from_data    = model.vertex_data[:,:3]
# Map model.point_indices onto model.vertex_points (reshape for comparison purposes)
points_from_indices = np.reshape(model.vertex_points[model.point_indices], (len(points_from_data), 3))

# These will yeild the same result
assert (points_from_data == points_from_indices).all()