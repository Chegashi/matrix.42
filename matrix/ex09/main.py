#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector

def main():
   m1 = Matrix([[0, 0], [0, 0]])
   print('______T[0, 0], [0, 0]] =')
   print(m1.transpose())

   m1 = Matrix([[1, 0], [0, 1]])
   print('______T[1, 0], [0, 1]] =')
   print(m1.transpose())

   m1 =  Matrix([[1, 2], [3, 4]])
   print('______T[1, 2], [3, 4]] =')
   print(m1.transpose())

   m1 =   Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
   print('______T[[1, 0, 0], [0, 1, 0], [0, 0, 1]] =')
   print(m1.transpose())

   m1 =  Matrix([[1, 2], [3, 4], [5, 6]])
   print('______T[[1, 2], [3, 4], [5, 6]] =')
   print(m1.transpose())

   m1 = Matrix([[0, 2], [3, 4]])
   print('______T[0, 2], [3, 4]] =')
   print(m1.transpose())

   m1 = Matrix([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])
   print('______ [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]] =')
   print(m1.transpose())

   m1 = Matrix([[1,2], [11, 22], [10, 20], [15,25]])
   print('______ [[1,2], [11, 22], [10, 20], [15,25]] =')
   print(m1.transpose())

if __name__ == '__main__':
   main()