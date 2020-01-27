"""
HW01: triangle classification 
Author: Xinyi Ye
Date: 01/27/2020
"""
from collections import defaultdict


def classify_triangle(a, b, c):
    """ classify_triangle() function: 
    return string to specify whether this triangle is is scalene, isosceles, or equilateral, 
    and whether it is right triangle as well
    """

    if all([isinstance(a, (int, float)), isinstance(b, (int, float)), isinstance(c, (int, float))]):
        """ if all the three lengths of triangle are numbers.""" 
        line = [a, b, c]
        line.sort()

        if any([a <= 0, b <= 0, c <= 0]):
            """ if the length number <= 0"""
            result = 'Error'

        elif line[0] + line[1] > line[2]:
            """ if the sum of any two sides is greater than the third side"""
            count = defaultdict(int)
            for m in line:
                count[m] += 1
            m = sorted(count.items(), key=lambda d: d[1], reverse=True)
            if m[0][1] == 1:
                result0 = 'this triangle is scalene'
            elif m[0][1] == 2:
                result0 = 'this triangle is isosceles'
            else:
                result0 = 'this triangle is equilateral'

            length1 = float(line[0])
            length2 = float(line[1])
            length3 = float(line[2])
            if round(((length1 ** 2) + (length2 ** 2)), 2) == round((length3 ** 2), 2):
                result1 = ' and it is also a right triangle'
            else:
                result1 = ' and it is not a right triangle'
            result = result0 + result1

        else:
            """ if the sum of any two sides is not greater that the third side"""
            result = 'it can not be a triangle'
        return result
    
    else:
        """ if the three lengths of triangle are not all numbers"""
        return 'Error'
