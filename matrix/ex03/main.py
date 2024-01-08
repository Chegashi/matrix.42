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
    # # // 2.0

    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(f"{s}print([-1., 6.].dot([3., 2.])){s}")
    print(u.dot(v))
    # // 9.0
    try:
        u = Vector([-1., 6., 3., 2.])
        v = Vector([3., 2.])
        print(u.dot(v))
    except Exception as e:
            TypeError (f"")
            print(f'ERROR: {e} :[-1., 6., 3., 2.] . [3., 2.] \n')

if __name__ == '__main__':
    main()
