"""
HW01_test: Testing triangle classification HW01
Author: Xinyi Ye
Date: 01/27/2020
"""
import unittest
import math
from hw01_xinyi_ye import classify_triangle


class BuggyTriangleTest(unittest.TestCase):
    """ BuggyTriangleTest class: test"""

    def test_classify_triangle(self):
        """ test HW01 classify_triangle() function"""

        t1_test = classify_triangle(4, 4, 4)
        t2_test = classify_triangle(2.768, 2.768, 2.768)
        t3_test = classify_triangle(2.0, 2, 2)
        self.assertTrue(
            t1_test == t2_test == t3_test ==
            'this triangle is equilateral and it is not a right triangle')

        t4_test = classify_triangle(2.1, 3, 2.1)
        t5_test = classify_triangle(2.1, 2.1, 3)
        t6_test = classify_triangle(3, 2.1, 2.1)
        t7_test = classify_triangle(3.0, 3, 2.7)
        self.assertTrue(
            t4_test == t5_test == t6_test == t7_test ==
            'this triangle is isosceles and it is not a right triangle')

        t8_test = classify_triangle(math.sqrt(2), math.sqrt(2), 2)
        t9_test = classify_triangle(math.sqrt(2), 2, math.sqrt(2))
        t10_test = classify_triangle(2, math.sqrt(2), math.sqrt(2))
        t11_test = classify_triangle(math.sqrt(8), math.sqrt(8), 4)
        self.assertTrue(
            t8_test == t9_test == t10_test == t11_test
            == 'this triangle is isosceles and it is also a right triangle')

        t12 = classify_triangle(2, 2, 5)
        t29 = classify_triangle(2, 5, 2)
        t30 = classify_triangle(5, 2, 2)
        self.assertTrue(t12 == t29 == t30 == 'it can not be a triangle')

        t13 = classify_triangle(2, 5, 4)
        t31 = classify_triangle(2, 4, 5)
        t32 = classify_triangle(5, 4, 2)
        t33 = classify_triangle(5, 2, 4)
        t34 = classify_triangle(4, 2, 5)
        t35 = classify_triangle(4, 5, 2)
        t14 = classify_triangle(3.5, 3, 6)
        t15 = classify_triangle(math.sqrt(8), math.sqrt(6), math.sqrt(3))
        self.assertTrue(
            t13 == t31 == t32 == t33 == t34 == t35 == t14 == t15
            == 'this triangle is scalene and it is not a right triangle')

        t16 = classify_triangle(3, 4, 5)
        t36 = classify_triangle(3, 5, 4)
        t37 = classify_triangle(4, 3, 5)
        t38 = classify_triangle(4, 5, 3)
        t39 = classify_triangle(5, 3, 4)
        t40 = classify_triangle(5, 4, 3)
        t17 = classify_triangle(6, 10, 8)
        t18 = classify_triangle(13.00000, 12, 5.0)
        t19 = classify_triangle(math.sqrt(2), math.sqrt(7), 3)
        self.assertTrue(
            t16 == t36 == t37 == t38 == t39 == t40 == t17 == t18 == t19
            == 'this triangle is scalene and it is also a right triangle')

        t20 = classify_triangle(5, 10, 15)
        t41 = classify_triangle(5, 15, 10)
        t42 = classify_triangle(10, 5, 15)
        t43 = classify_triangle(10, 15, 5)
        t44 = classify_triangle(15, 5, 10)
        t45 = classify_triangle(15, 10, 5)
        self.assertTrue(t20 == t41 == t42 == t43 == t44 ==
                        t45 == 'it can not be a triangle')

        t21 = classify_triangle(-1, 1, 3)
        t46 = classify_triangle(-1, 3, 1)
        t47 = classify_triangle(1, 3, -1)
        t48 = classify_triangle(1, -1, 3)
        t49 = classify_triangle(3, 1, -1)
        t50 = classify_triangle(3, -1, 1)
        t22 = classify_triangle(0, 3, 2)
        t23 = classify_triangle(-1, 0, 2)
        self.assertTrue(t21 == t46 == t47 == t48 == t49 ==
                        t50 == t22 == t23 == 'Error')

        t24 = classify_triangle('l', 3, 4)
        t51 = classify_triangle('l', 4, 3)
        t52 = classify_triangle(3, 'l', 4)
        t53 = classify_triangle(3, 4, 'l')
        t54 = classify_triangle(4, 'l', 3)
        t55 = classify_triangle(4, 3, 'l')
        t25 = classify_triangle('?', 3, 4)
        t26 = classify_triangle(' ', 3, 4)
        t27 = classify_triangle('', 3, 4)
        t28 = classify_triangle('asdki?j-', -1, 3)
        self.assertTrue(t24 == t51 == t52 == t53 == t54 == t55 == t25 == t26 ==
                        t27 == t28 == 'Error')


if __name__ == "__main__":

    unittest.main(exit=False, verbosity=2)
