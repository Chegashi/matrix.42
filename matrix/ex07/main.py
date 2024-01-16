#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   print("Matrix([[0, 0], [0, 0]]).mul_vec(Vector([10, 10]))")
   print(Matrix([[0, 0], [0, 0]]).mul_vec(Vector([10, 10])))
   
   print("Matrix([[1, 0], [0, 1]]).mul_vec(Vector([10, 10]))")
   print(Matrix([[1, 0], [0, 1]]).mul_vec(Vector([10, 10])))
   
   print("Matrix([[1, 1], [1, 1]]).mul_vec(Vector([4, 2]))")
   print(Matrix( [[1, 1], [1, 1]]).mul_vec(Vector([4, 2])))

   print("Matrix([[2, 0], [0, 2]]).mul_vec(Vector([2, 1]))")
   print(Matrix( [[2, 0], [0, 2]]).mul_vec(Vector([2, 1])))

   print("Matrix([[0.5, 0], [0, 0.5]]).mul_vec(Vector([4, 2]))")
   print(Matrix( [[0.5, 0], [0, 0.5]]).mul_vec(Vector([4, 2])))

   u = Matrix([[1., 0.], [0., 1.]])
   v = Vector([4., 2.])
   print("_____________[[1., 0.], [0., 1.]]).mul_vec([4., 2.])")
   print(f"{u.mul_vec(v)}")
   # // [4.]
   # // [2.]

   u = Matrix([[2., 0.], [0., 2.]])
   v = Vector([4., 2.])
   print("_____________[[[2., 0.], [0., 2.]]).mul_vec([4., 2.])")
   print(f"{u.mul_vec(v)}")
   # // [8.]
   # // [4.]

   u = Matrix([[2., -2.], [-2., 2.],])
   v = Vector([4., 2.])
   print("_____________[[2., -2.], [-2., 2.],]).mul_vec([4., 2.])")
   print(f"{u.mul_vec(v)}")
   # // [4.]
   # // [-4.]

   u = Matrix([[1., 0.],[0., 1.],])
   v = Matrix([[1., 0.],[0., 1.],])
   print("_____________[[1., 0.],[0., 1.],]).mul_vec([[1., 0.],[0., 1.],])")
   print(f"{u.mul_mat(v)}")
   # # // [1., 0.]
   # # // [0., 1.]

   u = Matrix([[1., 0.],[0., 1.],])
   v = Matrix([[2., 1.],[4., 2.],])
   print("_____________[[1., 0.],[0., 1.],]).mul_vec([[2., 1.],[4., 2.],])")
   print(f"{u.mul_mat(v)}")
   # // [2., 1.]
   # // [4., 2.]

   u = Matrix([[3., -5.],[6., 8.],])
   v = Matrix([[2., 1.],[4., 2.],])
   print("_____________[-14., -7.],[0., 1.],]).mul_vec([44., 22.])")
   print(f"{u.mul_mat(v)}", )
   # // [-14., -7.]
   # // [44., 22.]

   try:
      u = Matrix([[3., -5.],[6., 8.],[6., 8.]])
      print("_____________ [[3., -5.],[6., 8.],[6., 8.]] * [[3., -5.],[6., 8.],[6., 8.]] ")
      print(f"{u.mul_mat(u)}", )
      print(u)
   except Exception as e:
      print(f"ERROR: {e}")
       

   


if __name__ == '__main__':
    main()