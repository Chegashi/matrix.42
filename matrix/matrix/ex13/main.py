#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   print("Matrix([[0, 0], [0, 0]]).rank()")
   print( Matrix([[0, 0], [0, 0]]).rank())

   print("Matrix([[1, 0], [0, 1]]).rank()")
   print( Matrix([[1, 0], [0, 1]]).rank())
   
   print("Matrix([[2, 0], [0, 2]]).rank()")
   print( Matrix([[2, 0], [0, 2]]).rank())

   print("Matrix([[1, 1], [1, 1]]).rank()")
   print( Matrix([[1, 1], [1, 1]]).rank())

   print("Matrix([[0, 1], [1, 0]]).rank()")
   print( Matrix([[0, 1], [1, 0]]).rank())

   print("Matrix([[1, 2], [3, 4]]).rank()")
   print( Matrix([[1, 2], [3, 4]]).rank())

   print("Matrix([[-7, 5], [4, 6]]).rank()")
   print( Matrix([[-7, 5], [4, 6]]).rank())

   print("Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).rank()")
   print( Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).rank())
   print("______________________")
   
   u = Matrix([
   [1., 0., 0.],
   [0., 1., 0.],
   [0., 0., 1.],])
   print(u.rank())
   # // 3
   print("______________________")


   u = Matrix([
   [ 1., 2., 0., 0.],
   [ 2., 4., 0., 0.],
   [-1., 2., 1., 1.],])
   print(u.rank())
   # // 2
   print("______________________")

   u = Matrix([
   [ 8., 5., -2.],
   [ 4., 7., 20.],
   [ 7., 6., 1.],
   [21., 18., 7.],])
   print(u.rank())
   # // 3


if __name__ == '__main__':
    main()