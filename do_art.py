from PIL import Image, ImageFilter
import random
import os

def do_art(s):
    #define size of image
    size_image = (600, 800)

    #Random integer for degree of blur
    blur = random.randint(10, 25)
    print (blur)
    #List of conversions

    #Open the file by filename s
    image1 = Image.open(s)
    fn, fext = s.split(".")

    #### Randomly manipulate the image

    ## Blur the image
    image1 = image1.filter(ImageFilter.GaussianBlur(blur)).save(fn+ str(blur) +'.'+fext)




def main():
    do_art('45th Anniversary.jpg')

main()
