 #!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def angle_cos(u, v) -> float:
    return u.dot(v) / ((u.norm_0() * v.norm_0()) ** 0.5)

def main():
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(f"{angle_cos(u, v)}")
    # // 1.0
    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(f"{angle_cos(u, v)}")
    # // 0.0
    u = Vector([-1., 1.])
    v = Vector([ 1., -1.])
    print(f"{angle_cos(u, v)}")
    # // -1.0
    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(f"{angle_cos(u, v)}")
    # // 1.0
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(f"{angle_cos(u, v)}")
    # // 0.974631846

if __name__ == '__main__':
    main()