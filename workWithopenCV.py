import cv2
import numpy as np
from objects import goose, wolf, goose_name, wolf_name
from main import plot_2d_object

goose = goose.reshape((-1, 1, 2)).astype(np.float32)
wolf = wolf.reshape((-1, 1, 2)).astype(np.float32)

plot_2d_object(goose[:, 0], 'Initial goose', 'black', 3)
plot_2d_object(wolf[:, 0], 'Initial wolf', 'black', 3)

def rotate(object_name, object, degree):
    matrix = cv2.getRotationMatrix2D((0, 0), -degree, 1 )
    object = cv2.transform(object, matrix)
    plot_2d_object(object[:, 0], f'{object_name} rotated by {degree} degrees', 'purple', 3 )
    print( object[:, 0] )
def scale(object_name, object, scalar):
    matrix = cv2.getRotationMatrix2D( (0, 0), 0, scalar )
    object = cv2.transform( object, matrix )
    plot_2d_object( object[:, 0], f'{object_name} scaled by {scalar}', 'black', 3 )
    print(object[:, 0])

    print( cv2.getRotationMatrix2D((0, 0), 0, 1 ))

def shear(object_name, object, constant, axis, axis2=None):
    if axis == 'x' and axis2==None:
        matrix = np.float32([[1, constant, 0], [0, 1, 0]])
        object = cv2.transform(object, matrix)
        plot_2d_object( object[:, 0], f'{object_name} sheared by {constant} in {axis}-axis', 'green', 3 )
    elif axis == 'y' and  axis2==None:
        matrix = np.float32( [[1, constant, 0], [constant, 1, 0]] )
        object = cv2.transform( object, matrix )
        plot_2d_object( object[:, 0], f'{object_name} sheared by {constant} in {axis}-axis', 'green', 3 )
    else:
        matrix = np.float32([[1, constant, 0], [constant, 1, 0]] )
        object = cv2.transform( object, matrix )
        plot_2d_object(object[:, 0], f'{object_name} sheared by {constant} in both directions', 'grey', 3 )

def mirror (object_name, object, axis: str):
    axis = axis.lower()
    if axis == 'x':
        matrix = np.float32([[1, 0, 0], [0, -1, 0]])
    else:
        matrix = np.float32([[-1, 0, 0], [0, 1, 0]])
    object = cv2.transform(object, matrix)
    plot_2d_object( object[:, 0], f'{object_name} mirrored through {axis}-axis', 'yellow', 3 )

shear(goose_name, goose, 0.5, 'x')
shear(goose_name, goose, 0.5, 'y')
shear(goose_name, goose, 0.5, 'x', 'y')
shear(wolf_name, wolf, 0.5, 'x')
shear(wolf_name, wolf, 0.5, 'y')
shear(wolf_name, wolf, 0.5, 'x', 'y')

rotate(goose_name, goose, 90)
rotate(wolf_name, wolf, 90)

scale(goose_name, goose, 2)
scale(wolf_name, wolf, 2)

mirror( goose_name, goose, 'x' )
mirror( goose_name, goose, 'y' )
mirror( wolf_name, wolf, 'x' )
mirror( wolf_name, wolf, 'y' )
