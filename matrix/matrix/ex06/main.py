#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def cross_product(u, v) -> Vector:
    a, b, c = tuple(u.get_data())
    x, y, z = tuple(v.get_data())
    return Vector([b * z - c * y, c * x - a * z, a * y - x * b])

def main():
    print("cross_product(Vector([0., 0., 0.]), Vector([0., 0., 0.]))")
    print(cross_product(Vector([0., 0., 0.]), Vector([0., 0., 0.])))

    print("cross_product(Vector([1., 0., 0.]), Vector([0., 0., 0.]))")
    print( cross_product(Vector([1, 0., 0.]), Vector([0., 0., 0.])))

    print("cross_product(Vector([1., 0., 0.]), Vector([0., 1, 0]))")
    print( cross_product(Vector([1, 0., 0.]), Vector([0., 1,  0])))
   
    print("cross_product(Vector([8, 7, -4]), Vector([3, 2, 1]))")
    print( cross_product(Vector([8, 7, -4]), Vector([3, 2, 1])))

    print("cross_product(Vector([1, 1, 1]), Vector([0, 0, 0]))")
    print( cross_product(Vector([1, 1, 1]), Vector([0, 0, 0]))) 
    
    print("cross_product(Vector([1, 1, 1]), Vector([1, 1, 1]))")
    print( cross_product(Vector([1, 1, 1]), Vector([1, 1, 1])))  
    
    
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print("_________cross_product([0., 0., 1.],[1., 0., 0.])")
    print(f"{cross_product(u, v)}")
    # // [0.]
    # // [1.]
    # // [0.]

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print("_________cross_product([1., 2., 3.],[4., 5., 6.])")
    print(f"{cross_product(u, v)}")
    # // [-3.]
    # // [6.]
    # // [-3.]

    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print("_________cross_product([4., 2., -3.],[-2., -5., 16.])")
    print(f"{cross_product(u, v)}")
    # // [17.]
    # // [-58.]
    # // [-16.]

if __name__ == '__main__':
    main()