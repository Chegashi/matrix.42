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
    ei1 = Vector([ft_complex(0, 1), 0, 0])
    ei2 = Vector([0, ft_complex(0, 1), 0])
    ei3 = Vector([0, 0, ft_complex(0, 1)])
    
    vi2 = Vector([0, ft_complex(10, 10), -100])
    vi1 = Vector([ft_complex(0, 1), 2, 3])

    print("ei1 = [i, 0, 0]\n"
          "ei2 = [0, i, 0]\n"
          "ei3 = [0, 0, i]\n"
    )

    print("_________{linear_combination([ei1, ei2, ei3], [10, -2,0.5])}_________")
    print(f"{linear_combination([ei1, ei2, ei3], [10, -2,0.5])}")
    # [10i]
    # [-2i]
    # [0.5i]
    print("_________{linear_combination([ei1, ei2, ei3], [10, -2,0.5])}_________")
    print(f"{linear_combination([vi1, vi2], [10, -2])}")
    # [10i]
    # [-2i]
    # [230]

