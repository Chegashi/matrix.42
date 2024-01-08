#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def linear_combination(vectors, coefs):
    V = Vector([0,0,0])
    for k , v in zip(coefs, vectors):
        v.scl(k)
        V.add(v)
    return V

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


