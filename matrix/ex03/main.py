#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex


def main():
    s = "_________"
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(f"{s}print([0., 0.].dot([1., 1.])){s}")
    print(u.dot(v))
    # # // 0.0

    v = Vector([1., 1.])
    u = Vector([1., 1.])
    print(f"{s}print([1., 1.].dot([1., 1.])){s}")
    print(u.dot(v))

    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(f"{s}print([-1., 6.].dot([3., 2.])){s}")
    print(u.dot(v))
    # // 9.0

    u = Vector([0., 0.])
    v = Vector([ft_complex(1, 2), 1.])
    print(f"{s}print([0., 0.].dot([1+2i, 1])){s}")
    print(u.dot(v))
    # // 0.0

    v = Vector([ft_complex(1,2),ft_complex(1,2)])
    u = Vector([ft_complex(1,2), ft_complex(1,2)])
    print(f"{s}print([1+2i, 1+2i].dot([1+2i, 1+2i])){s}")
    print(u.dot(v))
    #  -6+8i

    u = Vector([ft_complex(3,2), 6.])
    v = Vector([ft_complex(1,3), 2.])
    print(f"{s}print([3+2i, 6].dot([1+3i, 2])){s}")
    print(u.dot(v))
    # 9.0+11i
    

if __name__ == '__main__':
    main()