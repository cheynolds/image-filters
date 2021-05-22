"""
This program implements an image filter by adjustments to RGB pixels.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def main():
    # Get file and load image
    filename = get_file()
    new_image = SimpleImage(filename)

    # Show the image before the transform
    new_image.show()

    for x in range(new_image.width):
        for y in range(new_image.height):
                pixel = new_image.get_pixel(x,y)
                pixel.red = pixel.red * 1.5
                pixel.blue = pixel.blue * 1.5
                pixel.green = pixel.green * 0.7
    # Show the image after the transform
    new_image.show()


def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
