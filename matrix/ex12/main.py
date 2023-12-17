#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([
   [1., 0., 0.],
   [0., 1., 0.],
   [0., 0., 1.],
   ])
   print(u.inverse())

   print('_____________')
   # //  [1.0, 0.0, 0.0]
   # //  [0.0, 1.0, 0.0]
   # //  [0.0, 0.0, 1.0]
   u = Matrix([
   [2., 0., 0.],
   [0., 2., 0.],
   [0., 0., 2.],
   ])
   print(u.inverse())
   print('_____________')
   # //  [0.5, 0.0, 0.0]
   # //  [0.0, 0.5, 0.0]
   # //  [0.0, 0.0, 0.5]
   u = Matrix([
   [8., 5., -2.],
   [4., 7., 20.],
   [7., 6., 1.],
   ])
   # print(u.adj())
   print(u.inverse())

   # //  [0.649425287, 0.097701149, -0.655172414]
   # //  [-0.781609195, -0.126436782, 0.965517241]
   # //  [0.143678161, 0.074712644, -0.206896552]



   

if __name__ == '__main__':
    main()