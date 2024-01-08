 #!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def angle_cos(u, v) -> float:
    try:
        d = u.dot(v) / ((u.norm_0() * v.norm_0()) ** 0.5)
        return d
    except Exception:
        return float('inf') 

def main():
    u = Vector([ft_complex(1,1), 0.])
    v = Vector([ft_complex(1,1), 0.])
    print(f"____________cos([1., 0.],[1., 0.])____________")
    print(f"{angle_cos(u, v)}")

    u = Vector([ft_complex(1,1), 0.])
    v = Vector([0., ft_complex(1,1)])
    print(f"____________cos([1+i, 0.],[0., 1+i])____________")
    print(f"{angle_cos(u, v)}")

    u = Vector([ft_complex(-1, 1), ft_complex(1+1)])
    v = Vector([ft_complex( 1, 1), ft_complex(-1+1)])
    print(f"____________cos([-1+i, 1+i.],[1+i., -1+i])____________")
    print(f"{angle_cos(u, v)}")

    u = Vector([ft_complex(2,1), ft_complex(1, 1)])
    v = Vector([ft_complex(4,1), ft_complex(2, 1)])
    print(f"____________cos([2+i, 1+i],[4+i, 2+i])____________")
    print(f"{angle_cos(u, v)}")

    u = Vector([ft_complex(1,1), 2., ft_complex(1,3)])
    v = Vector([ft_complex(1,4), 5., ft_complex(1,6)])
    print(f"____________cos([1+i,2, 1+3i],[1 + 4i, 5., 1+6i])____________")
    print(f"{angle_cos(u, v)}")

if __name__ == '__main__':
    main()