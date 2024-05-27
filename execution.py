from objects import *
from mainFunctionsForPart1 import *

plot_2d_object( goose, 'Goose', 'purple', 3 )
plot_2d_object( wolf, 'Wolf', 'purple', 3 )
plot_3d_object( object_3d, 'Object in 3d', 'green' )

rotate(goose_name, goose, 90)
rotate(wolf_name, wolf, 90)
rotate(object_3d_name, object_3d, 90, 'x')
rotate(object_3d_name, object_3d, 90, 'y')
rotate(object_3d_name, object_3d, 90, 'z')

scale(goose_name, goose, 5)
scale(wolf_name, wolf, 5)
scale(object_3d_name, object_3d, 5)

mirror(goose_name, goose, 'x')
mirror(goose_name, goose, 'y')
mirror(wolf_name, wolf, 'x')
mirror(wolf_name, wolf, 'y')
mirror(object_3d_name, object_3d, 'x')
mirror(object_3d_name, object_3d, 'y')
mirror(object_3d_name, object_3d, 'z')

shear_by_degree(goose_name, goose, 'x', 30)
shear_by_degree(goose_name, goose, 'y', 30)
shear_by_degree(goose_name, goose, 'y', 30, 'x')
shear_by_degree(wolf_name, wolf, 'x', 30)
shear_by_degree(wolf_name, wolf, 'y', 30)
shear_by_degree(wolf_name, wolf, 'y', 30, 'x')

shear_by_constant(goose_name, goose, 'x', 2)
shear_by_constant(goose_name, goose, 'y', 2)
shear_by_constant(goose_name, goose, 'y', 2, 'x')
shear_by_constant(wolf_name, wolf, 'x', 2)
shear_by_constant(wolf_name, wolf, 'y', 2)
shear_by_constant(wolf_name, wolf, 'y', 2, 'x')

universal( goose_name, goose, np.array( [[1, 7], [5, 6]] ) )
universal( wolf_name, wolf, np.array( [[1, 7], [5, 6]] ) )
universal( object_3d_name, object_3d, np.array( [[1, 7, 89], [5, 6, 5], [-6, -9, 7]] ) )

