#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex


def main():
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(u.dot(v))
    # // 0.0
    v = Vector([1., 1.])
    u = Vector([1., 1.])
    print(u.dot(v))
    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(u.dot(v))
    # // 9.0

    u = Vector([0., 0.])
    v = Vector([ft_complex(1, 2), 1.])
    print(u.dot(v))
    # // 0.0
    v = Vector([ft_complex(1,2),ft_complex(1,2)])
    u = Vector([ft_complex(1,2), ft_complex(1,2)])
    print(u.dot(v))
    #  -6+8i
    u = Vector([ft_complex(3,2), 6.])
    v = Vector([ft_complex(1,3), 2.])
    print(u.dot(v))
    # 9.0+11i
    

if __name__ == '__main__':
    main()