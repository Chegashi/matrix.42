#!/usr/bin/env pyhton

import sys
import numpy as np
sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([[ft_complex(1,1), 0., 0.], [0., ft_complex(1, 1), 0.], [0, 0, ft_complex(1)]])
   print(f"______________________________________________________\n")
   print(u.row_echelon())

   u = Matrix([[ft_complex(1,1), ft_complex(2,2)], [ft_complex(1,13), 4]])
   print(f"______________________________________________________\n")
   print(u.row_echelon())


   u = Matrix([[ft_complex(0,8), 5., -2., 4., 28.],
               [4., 2.5, ft_complex(1,1), 4., -4.],
               [8., 5., ft_complex(1,1), 4., 17.]])
 
   print(f"______________________________________________________\n")
   print(u.row_echelon())

if __name__ == '__main__':
    main()

