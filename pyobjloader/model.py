import os
import numpy as np


class Model:
    """
    Instance of a loaded model. Contains all objects, groups, and vertex data
    model.vertex_array contains all vertex data
    Objects stored in the model.objects dictionary, where keys are the object names (marked by 'o') in the .obj
    Default object key is '0'
    """
    
    def __init__(self) -> None:
        self.objects = {0 : VertexObject()}

        self.vertex_array = []

        self.vertex_points = []
        self.vertex_uv = []
        self.vertex_normals = []

    def __repr__(self) -> str:
        return_string = '<Model | objects: {'
        for vertex_object in self.objects.keys():
            return_string += str(vertex_object) + ', '
        return_string = return_string[:-2] + '}>'
        return return_string


class VertexObject:
    """
    Object conataining groups of vertices.
    Groups stored in the vertex_object.groups dictionary, where keys are the group names (marked by 'g') in the .obj
    Default group key is '0'
    """
    
    def __init__(self) -> None:
        self.groups = {0 : VertexGroup()}

    def __repr__(self) -> str:
        return_string = '<Vertex Object | groups: {'
        for vertex_group in self.groups.keys():
            return_string += str(vertex_group) + ', '
        return_string = return_string[:-2] + '}>'
        return return_string


class VertexGroup:
    """
    Groups containing the vertex data
    vertex_group.vertex_array will be a numpy array of vertices
    """
    
    def __init__(self) -> None:
        self.vertex_array = []

    def __repr__(self) -> str:
        return f'<Vertex Group | {self.vertex_array}>'


def load_model(directory: str) -> Model:
    """
    Loads an obj model. Returns a model class instance 
    model.vertex_array contains all vertex data combined in a single numpy array
    Args:
        directory: Path to the folder containing the .obj, .mtl, and any textures images 
    """

    obj_file = None
    mtl_file = None
    texture_file = None

    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        # Get the .obj file
        if filename.endswith(".obj") or filename.endswith(".py"):
            obj_file = os.path.join(directory, filename)

        # Get the .mtl file
        if filename.endswith(".mtl") or filename.endswith(".py"):
            mtl_file = os.path.join(directory, filename)

        #  Get texture files
        if filename.endswith(".png") or filename.endswith(".py"):
            texture_file = os.path.join(directory, filename)

    model = Model()
    current_object = 0
    current_group = 0

    with open(obj_file, 'r') as file:
        line = file.readline()
        while line:
            line = line.strip()

            # Add object
            if line.startswith('o '):
                if line[2:].strip() not in model.objects:
                    model.objects[line[2:].strip()] = VertexObject()
                current_object = line[2:].strip()

            # Add group
            elif line.startswith('g '):
                if line[2:].strip() not in model.objects[current_object].groups:
                    model.objects[current_object].groups[line[2:].strip()] = VertexGroup()
                current_group = line[2:].strip()

            # Add vertex point
            elif line.startswith('v '):
                points = list(map(float, line[2:].strip().split(' ')))
                model.vertex_points.append(points)
            
            # Add vertex UV
            elif line.startswith('vt '):
                uvs = list(map(float, line[3:].strip().split(' ')))
                model.vertex_uv.append(uvs[:2])

            # Add vertex normals
            elif line.startswith('vn '):
                normals = list(map(float, line[3:].strip().split(' ')))
                model.vertex_normals.append(normals)

            # Create faces
            elif line.startswith('f '):
                corners = line[2:].strip().split(' ')
                
                for corner_index, corner in enumerate(corners):
                    corner = list(map(int, corner.split('/')))

                    vertex = []

                    # Add each attribute to the vertex
                    for attribute, index in enumerate(corner):
                        if attribute == 0 and index:
                            vertex += model.vertex_points[index - 1]
                        if attribute == 1 and index:
                            vertex += model.vertex_uv[index - 1]
                        if attribute == 2 and index:
                            vertex += model.vertex_normals[index - 1]

                    # Replace the vertex data 
                    corners[corner_index] = vertex

                # Add each triangle to the objects vertex array
                for triangle in range(len(corners) - 2):
                    model.objects[current_object].groups[current_group].vertex_array.append(corners[0])
                    model.objects[current_object].groups[current_group].vertex_array.append(corners[1 + triangle])
                    model.objects[current_object].groups[current_group].vertex_array.append(corners[2 + triangle])

            line = file.readline()

    vertex_groups = []

    # Loop through all vertex objects and groups in the model
    for object in model.objects.values():
        for group in object.groups.values():
            # Ignore empty groups
            if not len(group.vertex_array): continue
            # Convert to a numpy array
            group.vertex_array = np.array(group.vertex_array, dtype='f4')
            # Add to the vertex_groups list to be stacked
            vertex_groups.append(group.vertex_array)

    # Array of all vertices from all the model's groups combined
    vertices = np.vstack(vertex_groups, dtype='f4')

    # Save the model's combined vertices
    model.vertex_array = vertices

    return model