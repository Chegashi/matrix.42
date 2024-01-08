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

    u = Vector([ft_complex(1, 1), ft_complex(1, 2), ft_complex(1, 3)])
    print(f"{s}([1 + i, 1 + 2, 1 + 3]{s}")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 6.0, 3.74165738, 3.0
    u = Vector([ft_complex(-1, -1), ft_complex(-2, 2)])
    print(f"{s}([[-1-i, -2+2i.]{s}")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 3.0, 2.236067977, 2.0

if __name__ == '__main__':
    main()