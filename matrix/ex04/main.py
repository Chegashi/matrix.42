#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex


def main():
    s = "_____________"
    u = Vector([0., 0., 0.])
    # print(f"{u.norm_1()}")
    print(f"u.norm_1(), u.norm(), u.norm_inf(){s}")

    print(f"{s}([0., 0., 0.]{s}")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 0.0, 0.0, 0.0
    u = Vector([1., 2., 3.])
    print(f"{s}([1., 2., 3.]{s}")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 6.0, 3.74165738, 3.0
    u = Vector([-1., -2.])
    print(f"{s}([[-1., -2.]{s}")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 3.0, 2.236067977, 2.0

if __name__ == '__main__':
    main()