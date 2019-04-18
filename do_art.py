from PIL import Image, ImageFilter, ImageDraw
import random
import os

def do_art(s):
    #define size of image
    size_image = (600, 800)

    #Random integer for degree of blur
    blur = random.randint(10, 25)
    print (blur)

    ######List of conversions#####
    #positions
    c21 = 1800 - 200*random.randint(1,10)
    c22 = 1800 - 120*random.randint(1,10)
    c23 = 1800 - 110*random.randint(1, 10)
    c24 = 1800 - 150*random.randint(1,10)
    c25 = 1800 - 160*random.randint(1,10)
    c25 = 10*random.randint(1,10)
    c27 = 10*random.randint(1,10)
    c28 = 10*random.randint(1,10)


    c1 = 100*random.randint(1,10)
    c2 = 500*random.randint(1,10)
    c3 = 700 * random.randint(1, 10)
    c4 = 560 * random.randint(1, 10)
    c5 = 300 * random.randint(1, 10)
    c6 = 250 * random.randint(1, 10)
    c7 = 600 * random.randint(1, 10)
    c8 = 125 * random.randint(1, 10)
    c9 = 163 * random.randint(1, 10)
    c10 = 146 * random.randint(1, 10)
    #Open the file by filename s
    image1 = Image.open(s)
    fn, fext = s.split(".")

    #### Randomly manipulate the image

    #Draw a line
    draw = ImageDraw.Draw(image1)
    draw.line((c1, c1) + size_image, fill=500, width=200)
    draw.line((0, size_image[1], size_image[0], 0), fill=128, width=200)
    draw.line((c6, c6) + (1200, 1600), fill=500, width=200)
    draw.line((c21,c22) + (c1, c3), fill=500, width=1000)
    draw.line((c21, c22)+ size_image, fill=500, width=1000)

    #Draw an Ellipse
    draw.ellipse([(c2, c3),(c4,c4)],fill=1,width=300,outline=400)
    draw.ellipse([(c5, c5), (c6, c6)], fill=256, width=300, outline=400)
    draw.ellipse([(c7, c7), (c8, c8)], fill=312, width=300, outline=400)
    draw.ellipse([(c9, c9), (c10, c10)], fill=500, width=300, outline=400)
    #image1.save(fn+ str(blur) +'.'+fext)



    ## Blur the image
    imFilter = image1.filter(ImageFilter.GaussianBlur(blur))
    image1.save(fn+ str(blur) +'.'+fext)




#def main():
#    do_art('45th Anniversary.jpg')

#main()
