import cv2 as cv
import numpy as np

image = cv.imread('dolphin.jpg')
assert image is not None, "File could not be read, check the path or file extension"
cv.imshow('Image', image)
cv.waitKey(0)

# scaling
scaled_image = cv.resize(image, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image', scaled_image)
cv.waitKey(0)

# mirroring
def mirror(image, axis: str):
    axis = axis.lower()
    if axis == 'x':
        mirrored_image = cv.flip(image, 0)
    else:
        mirrored_image = cv.flip(image, 1)
    cv.imshow(f'Mirrored Image around {axis}', mirrored_image)
    cv.waitKey(0)

mirror(image, 'x')
mirror(image, 'y')

# rotating
rows, cols, _ = image.shape
degree = 70
matrix = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), degree, 1 )
rotated_image = cv.warpAffine(image, matrix, (cols, rows))
cv.imshow(f'Rotated Image by {degree}', rotated_image)
cv.waitKey(0)

# shearing
constant = 0.5
M = np.float32([[1, constant, 0], [0, 1, 0], [0, 0, 1]])
sheared_image = cv.warpPerspective( image, M, (int( cols * 1.5 ), int( rows * 1.5 )) )
cv.imshow(f'Sheared  by {constant}', sheared_image )
cv.waitKey(0)
cv.destroyAllWindows()
