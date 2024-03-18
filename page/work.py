import sys
from PIL import Image
ASCII_CHARS = [' ','`','-','_',':','"',"'",'=','~','+','*','a','\\','/','|','1','2','(',')','[',']','<','>','?','7','0','#','$','&']
ASCII_CHARS.reverse()
ASCII_CHARS = ASCII_CHARS[::-1]
WIDTH = 85
def resize(image, new_width=WIDTH):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width)/2)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image
def grayscalify(image):
    return image.convert('L')
def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)
def do(image, new_width=WIDTH):
    image = resize(image)
    image = grayscalify(image)
    pixels = modify(image)
    len_pixels = len(pixels)
    new_image = [pixels[index:index+int(new_width)] for index in range(0, len_pixels, int(new_width))]
    return '\n'.join(new_image)
def load(file:int):
    image = None
    try:
        image = Image.open(f"./source/frame/{file}.jpg")
    except Exception:
        return
    return (do(image))