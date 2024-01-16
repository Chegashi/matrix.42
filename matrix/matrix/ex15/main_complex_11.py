#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([
      [ ft_complex(1,1), ft_complex(1,-1)],
      [ft_complex(1,-1), ft_complex(1,1)],
      ])
   print(u.determinant())
   print("______________")
   u = Matrix([
      [ft_complex(2,2), 0., 0.],
      [0., ft_complex(2,2), 0.],
      [0., 0., ft_complex(2,2)],
      ])
   print(u.determinant())
   print("______________")
   u = Matrix([
      [8., ft_complex(0,5), -2.],
      [4., 7., 20.],
      [7., 6., ft_complex(1,1)],
      ])
   print(u.determinant())
   print("______________")
   u = Matrix([
      [ 8., ft_complex(0,3), -2., 4.],
      [ 4., 2.5, 20., 4.],
      [ 8., 5., 1., 4.],
      [28., -4., 17., ft_complex(2,2)],
      ])
   print(u.determinant())

    

if __name__ == '__main__':
    main()
