#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([[ft_complex(1,-2), -8., 4.],[1., -23., 4.],[0., ft_complex(6,2), 4.],])
   print("___________trace([[1-2i, -8., 4.],[1., -23., 4.],[0., 6+2i., 4.],])")
   print(u.trace())
   # // -21.039
   u = Matrix([[ft_complex(1,2), ft_complex(1,2), 4.],[1., ft_complex(1,32), 4.],[0., 6., 4.],])
   print("___________trace([[1+2i., 1+2i, 4.],[1, 1+32i, 4.],[0., 6., 4.],])")
   print(u.trace())
   # 6.0+34i

if __name__ == '__main__':
    main()