"""
This program takes an image and generates a reflection.
The top half of the generated image is the same as the original.
The bottom half is the mirror reflection of the top half.
"""
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/mt-rainier.jpg'

def make_reflected(filename):
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    #create new image to contain mirror reflection
    reflected = SimpleImage.blank(width, height * 2)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x,y)
            reflected.set_pixel(x, y, pixel)
            reflected.set_pixel(x, (height*2)-(y+1) , pixel)
    return reflected

