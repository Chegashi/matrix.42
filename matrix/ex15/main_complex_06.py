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
    u = Vector([0., 0., ft_complex(1,1),])
    v = Vector([ft_complex(1,1), 0., 0.])
    print("_________cross_product([0., 0., 1+i],[1+i., 0., 0.])")
    print(f"{cross_product(u, v)}")

    u = Vector([ft_complex(1,1), ft_complex(1,2), ft_complex(1,3)])
    v = Vector([4., ft_complex(1,5), 6.])
    print("_________cross_product([1+i, 1+2i, 1+3i], [4., 1+5i, 6])")
    print(f"{cross_product(u, v)}")

    u = Vector([4., 2., ft_complex(1,-3)])
    v = Vector([ft_complex(1,-2), -5., ft_complex(16,16)])
    print("_________cross_product([4., 2., -3.],[-2., -5., 16.])")
    print(f"{cross_product(u, v)}")
    # // [17.]
    # // [-58.]
    # // [-16.]

if __name__ == '__main__':
    main()