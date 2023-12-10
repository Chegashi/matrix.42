#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def lerp(u, v,t):
    if not t:
        return u
    if t == 1:
        return v
    if isinstance(u, float) or isinstance(u, int) or isinstance(u, ft_complex):
        return (u + v) /2
    u.add(v)
    v.scl(0.5)
    return u

def main():
    print("_________lerp(0., 1., 0.)_________")
    print(lerp(0., 1., 0.))
    # // 0.0

    print("_________lerp(0., 1., 1.)_________")
    print(lerp(0., 1., 1.))
    # // 1.0

    print("_________print(lerp(0., 1., 0.5))_________")
    print(lerp(0., 1., 0.5))
    # // 0.5

    print("_________print(lerp(21., 42., 0.3))_________")
    print(lerp(21., 42., 0.3))
    # // 27.3

    print("_________lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3)_________")
    print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
    # // [2.6]
    # // [1.3]

    print("_________print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20.,10.], [30., 40.]]), 0.5))_________")
    print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20.,10.], [30., 40.]]), 0.5))
    # // [[11., 5.5]
    # // [16.5, 22.]]

    print("_________lerp(ft_complex(0,0), ft_complex(1,1), 0.)_________")
    print(lerp(ft_complex(0,0), ft_complex(1,1), 0.))
    # # // 0.0

    print("_________lerp(ft_complex(0,0), ft_complex(1,1), 1.)_________")
    print(lerp(ft_complex(0,0), ft_complex(1,1), 1.))
    # // 1+i

    print("_________llerp(0, ft_complex(1,1), 0.5)_________")
    print(lerp(0, ft_complex(1,1), 0.5))
    # # // 0.5 +0.5i

    print("_________llerp(ft_complex(1,12), ft_complex(42), 0.3)_________")
    print(lerp(ft_complex(1,12), ft_complex(42), 0.3))
    # # // 27.3

    print("_________lerp(Vector([2.,ft_complex(1,1)]), Vector([4., 2.]), 0.3)_________")
    print(lerp(Vector([2.,ft_complex(1,1)]), Vector([4., 2.]), 0.3))
    # # // [2.6]
    # # // [1.3]
    
if __name__ == '__main__':
    main()