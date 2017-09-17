''' Module that generates fractal flames images
    Warning: can produce errors cause of bad generated coefficients. Needs fixing.
    TODO: try out decimals module
'''
__author__ = "Alex Klim"

import argparse
from drawing import *


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='processing function arguments')
    parser.add_argument('--dots', help='number of dots on image', default=10000, type=int)
    parser.add_argument('--lc', help='number of affine transformations', default=5, type=int)
    parser.add_argument('--it', help='number of attractors', default=1000, type=int)
    parser.add_argument('--width', help='width of resulting image', default=1000, type=int)
    parser.add_argument('--height', help='height of resulting image', default=1000, type=int)

    args = parser.parse_args()
    image, coeffs = draw(**vars(args))
    
    #exporting results
    image.save("test.png", "PNG")
    with open('coeffs.txt', 'w') as outfile:
        json.dump(coeffs, outfile)
    with open('parameters.txt', 'w') as outfile:
        for arg in vars(args):
            outfile.write(str(vars(args)[arg]))
            outfile.write('\n')
    with open('non-linears.txt', 'w') as outfile:
        for func in non_linears:
            outfile.write(func.__name__)
            outfile.write('\n')