#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([[1., 0.],[0., 1.],])
   print("___________trace([[1., 0.],[0., 1.],])")
   print(u.trace())
   # // 2.0
   u = Matrix([[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.],])
   print("___________trace([[2., -5., 0.],[4., 3., 7.],[-2., 3., 4.],])")
   print(u.trace())
   # // 9.0
   u = Matrix([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.],])
   print("___________trace([[-2., -8., 4.],[1., -23., 4.],[0., 6., 4.],])")
   print(u.trace())
   # // -21.039
   u = Matrix([[ft_complex(1,2), ft_complex(1,2), 4.],[1., ft_complex(1,32), 4.],[0., 6., 4.],])
   print("___________trace([[1+2i., 1+2i, 4.],[1, 1+32i, 4.],[0., 6., 4.],])")
   print(u.trace())
   # 6.0+34i

if __name__ == '__main__':
    main()