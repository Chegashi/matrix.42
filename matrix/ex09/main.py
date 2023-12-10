#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   m1 = Matrix([[0, 2], [3, 4]])
   print('______T[0, 2], [3, 4]] = \n')
   print(m1.transpose())

   m1 = Matrix([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])
   print('______ [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]] = \n')
   print(m1.transpose())

   m1 = Matrix([[1,2], [11, 22], [10, 20], [15,25]])
   print('______ [[1,2], [11, 22], [10, 20], [15,25]] = \n')
   print(m1.transpose())

   m1 = Matrix([[0, ft_complex(1,1)], [ft_complex(3,3), ft_complex(5,4)]])
   print('______T[0, 1+i], [3+3i, 5+4i]] = \n')
   print(m1.transpose())

   m1 = Matrix([[1, 3, ft_complex(1,10), 7, 9], [2, ft_complex(1,-2), 6, 8, 10]])
   print('______ [[1, 3, 1+10i, 7, 9], [2, 1-2i, 6, 8, 10]] = \n')
   print(m1.transpose())

   m1 = Matrix([[1,2], [11, 22], [10, ft_complex(1337,-21)], [15,ft_complex(-2,14)]])
   print('______ [[1,2], [11, 22], [10, 1337-21i ], [15,-2+14i]] = \n')
   print(m1.transpose())


if __name__ == '__main__':
    main()