#!/usr/bin/env pyhton

import sys
import numpy as np
sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
   print(f"______________________________________________________\n"
         "Matrix[[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]"
         "\nexpect :\n[[1., 0., 0.], \n[0., 1., 0.], \n[0., 0., 1.]]] = \n result :")
   print(u.row_echelon())

   u = Matrix([[1, 2], [3, 4]])
   print(f"______________________________________________________\n"
         "Matrix[ [1., 2.],[3., 4.]"
         "\nexpect :\n [1.0, 0.0], \n [0.0, 1.0] = \n result :")
   print(u.row_echelon())


   u = Matrix([[8., 5., -2., 4., 28.],
               [4., 2.5, 20., 4., -4.],
               [8., 5., 1., 4., 17.]])
 
   print(f"______________________________________________________\n"
         "Matrix [[8., 5., -2., 4., 28.], [4., 2.5, 20., 4., -4.], [8., 5., 1., 4., 17.]]"
         "\nexpect :\n [1.0, 0.625, 0.0, 0.0, -12.1666667],\n [0.0, 0.0, 1.0, 0.0, -3.6666667],\n [0.0, 0.0, 0.0, 1.0, 29.5 ] = \n result :")
   print(u.row_echelon())

if __name__ == '__main__':
    main()

