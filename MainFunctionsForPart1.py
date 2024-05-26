from main import *
def rotate(object_name, object, degree, axis=None):
    if object.shape[1] == 2:
        plot_2d_object( rotate_object_by_degrees( object, degree ), f'{object_name} rotated by {degree} degrees', 'purple',
                        3 )
        print( rotate_object_by_degrees( object, degree ) )
    else:
        plot_3d_object( rotate_object_by_degrees( object, degree, axis ),
                        f'{object_name} rotated around {axis} by {degree} degrees', 'green' )
        print( rotate_object_by_degrees( object, degree, axis ) )


def scale(object_name, object, scalar):
    if object.shape[1] == 2:
        plot_2d_object( scale( object, scalar ), f'{object_name} scaled {scalar} times', 'purple', 3 )
        print( scale( object, scalar ) )
    else:
        plot_3d_object( scale( object, scalar ), f'{object_name} - scaled {scalar} times', 'green' )
        print( scale( object, scalar ) )


def mirror(object_name, object, axis):
    if object.shape[1] == 2:
        plot_2d_object( mirror_by_axis( object, axis ), f'{object_name} - mirrored {axis}', 'purple', 3 )
        print( mirror_by_axis( object, axis ) )
    else:
        plot_3d_object( mirror_by_axis( object, axis ), f'{object_name} - mirrored {axis}', 'green' )
        print( mirror_by_axis( object, axis ) )


def shear_by_degree(object_name, object, axis, degree):
    plot_2d_object( shear( object, axis, degree ), f'{object_name} - sheared by {degree} degrees towards {axis}', 'purple',
                    3 )
    print( shear( object, axis, degree ) )


def shear_by_constant(object_name, object, axis, constant):
    plot_2d_object( shear2( object, axis, constant ), f'{object_name} - sheared by {constant} towards {axis}', 'purple', 3 )
    print( shear2( object, axis, constant ) )


def universal(object_name, object, matrix):
    if object.shape[1] == 2:
        plot_2d_object( universal( object, matrix ), f'{object_name} transformed by matrix {matrix}', 'purple', 3 )
        print( universal( object, matrix ) )
    else:
        plot_3d_object( universal( object, matrix ),
                        f'{object_name} transformed by {matrix}', 'green' )
        print( universal( object, matrix ) )

