import os
import numpy as np


class Model:
    def __init__(self) -> None:
        self.objects = {0 : VertexObject()}

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
    def __init__(self) -> None:
        self.groups = {0 : VertexGroup()}

    def __repr__(self) -> str:
        return_string = '<Vertex Object | groups: {'
        for vertex_group in self.groups.keys():
            return_string += str(vertex_group) + ', '
        return_string = return_string[:-2] + '}>'
        return return_string


class VertexGroup:
    def __init__(self) -> None:
        self.vertices = []

    def __repr__(self) -> str:
        return f'<Vertex Group | {self.vertices}>'


def load_model(directory: str):
    """
    Loads an obj model. Returns an model instance
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

            # Add vertex normals
            elif line.startswith('f '):
                corners = line[2:].strip().split(' ')
                
                for corner_index, corner in enumerate(corners):
                    corner = list(map(int, corner.split('/')))

                    vertex = []

                    for attribute, index in enumerate(corner):
                        if attribute == 0 and index:
                            vertex += model.vertex_points[index - 1]
                        if attribute == 1 and index:
                            vertex += model.vertex_uv[index - 1]
                        if attribute == 2 and index:
                            vertex += model.vertex_normals[index - 1]

                    corners[corner_index] = vertex

                for triangle in range(len(corners) - 2):
                    model.objects[current_object].groups[current_group].vertices.append(corners[0])
                    model.objects[current_object].groups[current_group].vertices.append(corners[1 + triangle])
                    model.objects[current_object].groups[current_group].vertices.append(corners[2 + triangle])

            line = file.readline()

    vertex_groups = []

    for object in model.objects.values():
        for group in object.groups.values():
            if len(group.vertices):
                vertex_groups.append(group.vertices)

    vertices = np.vstack(vertex_groups, dtype='f4')

    return vertices