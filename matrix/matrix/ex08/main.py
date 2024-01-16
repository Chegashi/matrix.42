#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([[0, 0],[0, 0],])
   print("___________trace([[0, 0.],[0., 0],])")
   print(u.trace())
   
   u = Matrix([[1., 0],[0, 1],])
   print("___________trace([[1., 0],[0, 1],])")
   print(u.trace())
   
   u = Matrix([[1., 2.],[3., 4.],])
   print("___________trace([[1., 2.],[3., 4.],])")
   print(u.trace())

   u = Matrix([[8., -7.],[4., 2.],])
   print("___________trace([[8., -7.],[4., 2.],])")
   print(u.trace())
   

   u = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
   print("___________trace([[1, 0, 0], [0, 1, 0], [0, 0, 1]])")
   print(u.trace())
   
   
   u = Matrix([[1., 0.],[0., 1.],])
   print("___________trace([[1., 0.],[0., 1.],])")
   print(u.trace())
   
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

if __name__ == '__main__':
   main()
