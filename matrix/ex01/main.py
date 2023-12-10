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
    ei1 = Vector([ft_complex(0, 1), 0, 0])
    ei2 = Vector([0, ft_complex(0, 1), 0])
    ei3 = Vector([0, 0, ft_complex(0, 1)])
    
    v2 = Vector([0, 10, -100])
    v1 = Vector([1, 2, 3])
    vi2 = Vector([0, ft_complex(10, 10), -100])
    vi1 = Vector([ft_complex(0, 1), 2, 3])
    print(f"{linear_combination([e1, e2, e3], [10, -2,0.5])}")
    # [10.]
    # [-2.]
    # [0.5]
    print(f"{linear_combination([v1, v2], [10, -2])}")
    # [10.]
    # [0.]
    # [230.]
    print(f"{linear_combination([ei1, ei2, ei3], [10, -2,0.5])}")
    # [10i]
    # [-2i]
    # [0.5i]
    print(f"{linear_combination([vi1, vi2], [10, -2])}")
    # [10i]
    # [-2i]
    # [230]

