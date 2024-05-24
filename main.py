import numpy as np
import matplotlib.pyplot as plt
def plot_figure(coordinates, title, color, contour_width):
    plt.figure()
    plt.plot(coordinates[:, 0], coordinates[:, 1], "black", linewidth=contour_width)
    plt.fill(coordinates[:, 0], coordinates[:, 1], color)
    plt.title(title)
    plt.axis('equal')
    plt.grid(True)
    plt.show()
def rotate_object_by_degrees(object, degree):
    degree = np.radians(degree)
    rotation_matrix = np.array([[np.cos(degree), -np.sin(degree)], [np.sin(degree), np.cos(degree)]])
    object = np.dot(object, rotation_matrix)
    return object

goose = np.array([[-3, 9], [-1, 10], [-1, 11], [0, 12], [1.5, 11], [1.5, 7], [-0.5, 4], [-0.5, 3], [1, 2], [8, 2], [10, 5], [9, -1], [7, -4], [1, -4], [-2, 0], [-2, 4], [0, 7], [0, 9], [-3, 9]])
wolf = np.array([[-9, 5], [-7, 5], [-6, 6], [-5, 6], [-4, 7], [-4, 6], [-1, 3], [8, 3], [10, 1], [10, -4], [9, -5], [9, -1], [7, -7], [5, -7], [6, -6], [6, -4], [5, -2], [5, -1], [3, -2], [0, -1], [-3, -2], [-3, -7], [-5, -7], [-4, -6], [-4, -1], [-6, 3], [-9, 4], [-9, 5]])

plot_figure(goose, 'Goose', 'pink', 3)
plot_figure(wolf, 'Wolf', 'blue', 3)
plot_figure(rotate_object_by_degrees(goose, -20),'goose ', 'pink', 3)