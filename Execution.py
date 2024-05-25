from main import *
import numpy as np

# objects
goose = np.array([[-3, 9], [-1, 10], [-1, 11], [0, 12], [1.5, 11], [1.5, 7], [-0.5, 4], [-0.5, 3], [1, 2], [8, 2], [10, 5], [9, -1], [7, -4], [1, -4], [-2, 0], [-2, 4], [0, 7], [0, 9], [-3, 9]])
wolf = np.array([[-9, 5], [-7, 5], [-6, 6], [-5, 6], [-4, 7], [-4, 6], [-1, 3], [8, 3], [10, 1], [10, -4], [9, -5], [9, -1], [7, -7], [5, -7], [6, -6], [6, -4], [5, -2], [5, -1], [3, -2], [0, -1], [-3, -2], [-3, -7], [-5, -7], [-4, -6], [-4, -1], [-6, 3], [-9, 4], [-9, 5]])
object_3d = np.array([[1, 2, 3], [-4, 5, -6], [7, -8, 9], [-10, 11, -12], [13, 14, 15], [44, -4, 22], [45, 1, 2], [-3, -50, 18]])

# their pictures
plot_2d_object( goose, 'Goose', 'purple', 3 )
plot_2d_object( wolf, 'Wolf', 'blue', 3 )
plot_3d_object( object_3d, 'Object in 3d', 'green' )

# rotation by a specific degree
plot_2d_object( rotate_object_by_degrees( goose, 90 ), 'Goose - rotated', 'purple', 3 )
print( rotate_object_by_degrees( goose, 90 ))
plot_2d_object( rotate_object_by_degrees( wolf, 90), 'Wolf - rotated', 'blue', 3 )
print( rotate_object_by_degrees( wolf, 90 ))
plot_3d_object( rotate_object_by_degrees( object_3d, 90, 'x'), 'Object in 3d - rotated around x', 'green' )
print( rotate_object_by_degrees( object_3d, 90, 'x' ))
plot_3d_object( rotate_object_by_degrees( object_3d, 90, 'y'), 'Object in 3d - rotated around y', 'green' )
print( rotate_object_by_degrees( object_3d, 90, 'y' ))
plot_3d_object( rotate_object_by_degrees( object_3d, 90, 'z'), 'Object in 3d - rotated around z', 'green' )
print( rotate_object_by_degrees( object_3d, 90, 'z' ))

# scaling
plot_2d_object( scale( goose, 5 ), 'Goose - scaled', 'purple', 3 )
print( scale( goose, 5 ))
plot_2d_object( scale( wolf, 5 ), 'Wolf - scaled', 'blue', 3 )
print( scale( wolf, 5 ))
plot_3d_object( scale( object_3d, 5), 'Object in 3d - scaled', 'green' )
print( scale( object_3d, 5 ))

# mirroring
plot_2d_object( mirror_by_axis( goose, 'x' ), 'Goose - mirrored x', 'purple', 3 )
print(mirror_by_axis( goose, 'x' ))
plot_2d_object( mirror_by_axis( goose, 'y' ), 'Goose - mirrored y', 'purple', 3 )
print(mirror_by_axis( goose, 'y' ))
plot_2d_object( mirror_by_axis( wolf, 'x' ), 'Wolf -  mirrored x', 'blue', 3 )
print(mirror_by_axis( wolf, 'x' ))
plot_2d_object( mirror_by_axis( wolf, 'y' ), 'Wolf -  mirrored y', 'blue', 3 )
print(mirror_by_axis( wolf, 'y' ))
plot_3d_object( mirror_by_axis( object_3d, 'x' ), 'Object in 3d - mirrored x', 'green' )
print(mirror_by_axis( object_3d, 'x' ))
plot_3d_object( mirror_by_axis( object_3d, 'y' ), 'Object in 3d - mirrored y', 'green' )
print(mirror_by_axis( object_3d, 'y' ))
plot_3d_object( mirror_by_axis( object_3d, 'z' ), 'Object in 3d - mirrored z', 'green' )
print(mirror_by_axis( object_3d, 'z' ))

# shearing (degree)
plot_2d_object( shear( goose, 'x', 30 ), 'Goose - sheared, degree', 'purple', 3 )
print(shear( goose, 'x', 30 ))
plot_2d_object( shear( goose, 'y', 30 ), 'Goose - sheared, degree', 'purple', 3 )
print(shear( goose, 'y', 30 ))
plot_2d_object( shear( wolf, 'x', 30 ), 'Goose - sheared, degree', 'purple', 3 )
print( shear( wolf, 'x', 30 ) )
plot_2d_object( shear( wolf, 'y', 30 ), 'Wolf - sheared, degree', 'blue', 3 )
print(shear( wolf, 'y', 30 ))

# shearing (constant)
plot_2d_object( shear2( goose, 'x', 2 ), 'Goose - sheared, constant', 'purple', 3 )
print(shear( goose, 'x', 2 ))
plot_2d_object( shear2( goose, 'y', 2 ), 'Goose - sheared, constant', 'purple', 3 )
print(shear( goose, 'y', 2 ))
plot_2d_object( shear2( wolf, 'x', 2 ), 'Wolf - sheared, constant', 'blue', 3 )
print(shear( wolf, 'x', 2 ))
plot_2d_object( shear2( wolf, 'y', 2 ), 'Wolf - sheared, constant', 'blue', 3 )
print(shear( wolf, 'y', 2 ))

# universal
plot_2d_object(universal(goose, np.array([[1, 7], [5, 6]])), 'Goose - universal', 'purple', 3 )
print(universal(goose, np.array([[1, 7], [5, 6]])))
plot_2d_object(universal(wolf, np.array([[1, 7], [5, 6]])), 'Wolf - universal', 'blue', 3 )
print(universal(wolf, np.array([[1, 7], [5, 6]])))
plot_3d_object(universal(object_3d, np.array([[1, 7, 89], [5, 6, 5], [-6, -9, 7]])), 'Object in 3d - universal', 'green' )
print(universal(object_3d, np.array([[1, 7, 89], [5, 6, 5], [-6, -9, 7]])))

