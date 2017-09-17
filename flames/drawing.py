from PIL import Image, ImageDraw
from funcs import *


class Pixel:
    x=0
    y=0
    count = 0
    color = (0,0,0)
    normal = 0

def calculate (n, eqCount, it, xRes, yRes):
    XMIN=-1.777
    XMAX=1.777
    YMIN=-1
    YMAX=1
    coeff=[]
    pixels = {}
    # for loop that generates affine transformation coefficients
    for i in range(0,eqCount):
        coeff.append(gen_coeffs())
    # loop that generates image pixels
    for i in range(0,n):
        newX = uniform(XMIN, XMAX)
        newY = uniform(YMIN, YMAX)
        non_linear = non_linears[randint(0,5)]

        for step in range(-20,it):
            afin = randint(0,len(coeff)-1)
            x = coeff[afin][0] * newX + coeff[afin][1] * newY + coeff[afin][2]
            y = coeff[afin][3] * newX + coeff[afin][4] * newY + coeff[afin][5]
            newX, newY = non_linear(x,y)

            if step>=0 and newX<XMAX and newX>XMIN and newY<YMAX and newY>YMIN:
                x1 = xRes - math.trunc(((XMAX - newX) / (XMAX - XMIN)) * xRes)
                y1 = yRes - math.trunc(((YMAX - newY) / (YMAX - YMIN)) * yRes)
                if x1 < xRes and y1 < yRes: 
                    if str(x1)+","+str(y1) in pixels:
                        red = pixels[str(x1)+","+str(y1)].color[0]
                        green = pixels[str(x1)+","+str(y1)].color[1]
                        blue = pixels[str(x1)+","+str(y1)].color[2]

                        red = (red + coeff[afin][6][0]) // 2
                        green = (green + coeff[afin][6][1]) // 2
                        blue = (blue + coeff[afin][6][2]) // 2
                        pixels[str(x1)+","+str(y1)].count += 1
                        pixels[str(x1)+","+str(y1)].color = (red, green, blue)
                    else:
                        buf = Pixel()
                        buf.color = (coeff[afin][6][0], coeff[afin][6][1], coeff[afin][6][2])
                        buf.x = x1
                        buf.y = y1
                        pixels.update({str(x1)+","+str(y1):buf})
                        pixels[str(x1)+","+str(y1)].count = 0

    return pixels

def correction(pixels):
    maximus = 0.0
    gamma = 2.2
    for pixel in pixels:
        if pixels[pixel].count != 0:
            pixels[pixel].normal=math.log10(pixels[pixel].count)
            if pixels[pixel].normal > maximus:
                maximus = pixels[pixel].normal
    for pixel in pixels:
        pixels[pixel].normal /= maximus
        pixels[pixel].color = (math.trunc(pixels[pixel].color[0]*pow(pixels[pixel].normal,(1.0 / gamma))),
                               math.trunc(pixels[pixel].color[1]*pow(pixels[pixel].normal,(1.0 / gamma))),
                               math.trunc(pixels[pixel].color[2]*pow(pixels[pixel].normal,(1.0 / gamma))))
    return pixels

def draw(dots, lc, it, width, height):
    image = Image.new("RGBA", (width,height), "black")
    draw = ImageDraw.Draw(image)
    pixels = calculate(dots, lc, it, width, height)
    pixels = correction(pixels)
    for pix in pixels:
        draw.point([pixels[pix].x,pixels[pix].y], fill=pixels[pix].color)
    del draw
    image.save("test.png", "PNG")