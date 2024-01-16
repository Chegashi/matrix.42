#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def linear_combination(vectors, coefs):
    try:
        combin = Vector([0] * vectors[0].size[0])
        for k , v in zip(coefs, vectors):
            v.scl(k)
            # print(v)
            combin.add(v)
            # print(combin)
            # print('___')
        return combin
    except Exception as e:
        print(f"check if Vectors is empty or with diffrent size ({e})")

if __name__ == '__main__':
    e1 = Vector([1, 0, 0])
    e2 = Vector([0, 1, 0])
    e3 = Vector([0, 0, 1])
    
    v2 = Vector([0, 10, -100])
    v1 = Vector([1, 2, 3])

    print("e1 = [1, 0, 0]\n"
        "e2 = [0, 1, 0]\n"
        "e3 = [0, 0, 1]\n"
    )
    print("_________linear_combination([e1, e2, e3], [10, -2,0.5])_________")
    print(f"{linear_combination([e1, e2, e3], [10, -2, 0.5])}")
    # [10.]
    # [-2.]
    # [0.5]

    print("_________{linear_combination([v1, v2], [10, -2])}_________")
    print(f"{linear_combination([v1, v2], [10, -2])}")
    # [10.]
    # [0.]
    # [230.]
    
    
    print('linear_combination([Vector([-42., 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.])')
    print(linear_combination([Vector([-42., 42.])], [-1.]))

    print('linear_combination([Vector([-42]), Vector([-42]), Vector([-42])], [1., -1, 0])')
    print( linear_combination([Vector([-42]), Vector([-42]), Vector([-42])], [1., -1, 0]))

    print('linear_combination([Vector([-42., 42.]), Vector([1, 3]), Vector([10, 20])], [1., -10, -1])')
    print( linear_combination([Vector([-42., 42.]), Vector([1, 3]), Vector([10, 20])], [1., -10, -1]))
    
    print('linear_combination([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.])')
    print( linear_combination([Vector([-42., 100., -69.5]), Vector([1., 3., 5.])], [1., -10.]))


