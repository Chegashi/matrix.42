#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([[ft_complex(1,1), 0.],[0., ft_complex(2,2)],])
   v = Matrix([[2., 1.],[4., ft_complex(3,3)],])
   print("_____________[[1., 0.],[0., 1.],]).mul_vec([[2., 1.],[4., 2.],])")
   print(f"{u.mul_mat(v)}")
   #  // [[2.0+2.0i 1.0+i],
   #  // [8.0+8.0i 12i]]

   u = Matrix([[ft_complex(3,2), ft_complex(-5,8)],[ft_complex(0,6), ft_complex(0.-1)],])
   v = Matrix([[2., 1.],[4., 2.],])
   print("_____________[-14., -7.],[0., 1.],]).mul_vec([44., 22.])")
   print(f"{u.mul_mat(v)}", )
   # // [[-14.0+36.0i -7.0+18.0i],
   # // [-4.0+12.0i -2.0+6.0i]]

   


if __name__ == '__main__':
    main()