from functools import reduce
from ast import literal_eval as make_tuple

def parse_file(filename):
    file = open(filename)
    pyramid = []
    
    for line in file:
         pyramid.append(make_tuple(line))
    pyramid = tuple(pyramid)
    
    file.close()
    return pyramid

def sum_triangle(top, left, right):
    return top + max(left, right)
 
def integrate(lowerline, upperline):
    return list(map(sum_triangle, upperline, lowerline, lowerline[1:]))
 
def count_gold(pyramid):
    return reduce(integrate, reversed(pyramid)).pop()

if __name__ == "__main__":
    test_pyramid = (
        (1,),
        (1,2),
        (1,2,3),
        (1,2,3,4),
        (1,2,3,4,5),
        (1,2,3,4,5,6),
        (1,2,3,4,5,6,7)
    )
    pyramid = parse_file('pyramid.txt')
    print("Max sum is: ", count_gold(pyramid))
    print("Max sum(test pyramid) is: ", count_gold(test_pyramid))