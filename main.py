import numpy as np
import matplotlib.pyplot as plt
def plot_2d_object(object, title, color, contour_width):
    plt.figure()
    plt.plot(object[:, 0], object[:, 1], color="black", linewidth=contour_width)
    plt.fill(object[:, 0], object[:, 1], color)
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.show()
def plot_3d_object(object, title, color):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(object[:, 0], object[:, 1], object[:, 2], color=color)
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
def find_rotation_matrix_for_2D(degree: float):
    return np.array([[np.cos(degree), -np.sin(degree)], [np.sin(degree), np.cos(degree)]])

def find_rotation_matrix_for_3D(degree: float, axis: str):
    axis = axis.lower()
    if axis == 'x':
        return np.array( [
            [1, 0, 0],
            [0, np.cos(degree), -np.sin(degree)],
            [0, np.sin(degree), np.cos(degree)]
        ])
    elif axis == 'y':
        return np.array([
            [np.cos(degree), 0, np.sin(degree)],
            [0, 1, 0],
            [-np.sin(degree), 0, np.cos(degree)]
        ])
    elif axis == 'z':
        return np.array([
            [np.cos(degree), -np.sin(degree), 0],
            [np.sin(degree), np.cos(degree), 0],
            [0, 0, 1]
        ])


def rotate_object_by_degrees(object, degree: float, axis='-'):
    degree = np.radians(degree)
    rotation_matrix = None
    if object.shape[1] == 2:
        rotation_matrix = find_rotation_matrix_for_2D(degree)
    elif object.shape[1] == 3:
        rotation_matrix = find_rotation_matrix_for_3D(degree, axis)
    return np.dot(rotation_matrix, object.T).T


def scale(object, scalar: float):
    if object.shape[1] == 2:
        matrix = np.array([[scalar, 0],
                            [0, scalar]])
    else:
        matrix = np.array([[scalar, 0, 0],
                            [0, scalar, 0],
                            [0, 0, scalar]])
    return np.dot(matrix, object.T).T

def mirror_by_axis(object, axis: str):
    axis = axis.lower()
    matrix = None
    if axis == 'x':
        if object.shape[1] == 2:
            matrix = np.array([[1, 0], [0, -1]])
        elif object.shape[1] == 3:
            matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
    elif axis == 'y':
        if object.shape[1] == 2:
            matrix = np.array([[-1, 0], [0, 1]])
        elif object.shape[1] == 3:
            matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])
    elif axis == 'z' and object.shape[1] == 3:
        matrix = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    return np.dot(matrix, object.T).T

def shear(object, axis: str, degree: float):
    degree = np.radians(degree)
    if axis.lower() == 'x':
        matrix = np.array( [[1, np.tan(degree)], [0, 1]] )
    else:
        matrix = np.array( [[1, 0], [np.tan(degree), 1]] )

    return np.dot(matrix, object.T).T

def shear2(object, axis: str, constant: float):
    if axis.lower() == 'x':
        matrix = np.array( [[1, constant], [0, 1]] )
    else:
        matrix = np.array( [[1, 0], [constant, 1]] )

    return np.dot(matrix, object.T).T

def universal(object, matrix):
    return np.dot(matrix, object.T).T




