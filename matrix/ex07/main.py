#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([[1., 0.], [0., 1.]])
   v = Vector([4., 2.])
   print(f"{u.mul_vec(v)}")
   # // [4.]
   # // [2.]
   # u = Matrix([[2., 0.], [0., 2.]])
   # v = Vector([4., 2.])
   # print(f"{u.mul_vec(v)}")
   # # // [8.]
   # # // [4.]
   # u = Matrix([[2., -2.], [-2., 2.],])
   # v = Vector([4., 2.])
   # print(f"{u.mul_vec(v)}")
   # # // [4.]
   # # // [-4.]
   # u = Matrix([[1., 0.],[0., 1.],])
   # v = Matrix([[1., 0.],[0., 1.],])
   # print(f"{u.mul_mat(v)}")
   # # // [1., 0.]
   # # // [0., 1.]
   # # u = Matrix([[1., 0.],[0., 1.],])
   # # v = Matrix([[2., 1.],[4., 2.],])
   # print(f"{u.mul_mat(v)}")
   # # // [2., 1.]
   # # // [4., 2.]
   # u = Matrix([[3., -5.],[6., 8.],])
   # v = Matrix([[2., 1.],[4., 2.],])
   # print(f"{u.mul_mat(v)}", )
   # # // [-14., -7.]
   # # // [44., 22.]


if __name__ == '__main__':
    main()