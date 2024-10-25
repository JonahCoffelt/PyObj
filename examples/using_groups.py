"""
Example for accessing the data from a specific object/group

IMPORTANT:
    All objects are stored in the model
    Objects contain groups for acessing vertex data
    The method for storing the data in groups/objects varies from file to file
    So it is best print the object tree to you can access
"""

from pyobjloader import load_model

# Load the model from file
model = load_model("examples/models/cow.obj")

# Take a look at the tree
print(model.objects)

# Locate the specific data we want
leg_data = model.objects['leg2'].groups[0].vertex_data