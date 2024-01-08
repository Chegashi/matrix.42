#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
   u = Matrix([
   [ft_complex(1,1), 0., 0.],
   [0., ft_complex(1,1), 0.],
   [0., 0., ft_complex(1,1)],
   ])
   print(u.inverse())

   print('_____________')
   u = Matrix([
   [ft_complex(2,2), 0., 0.],
   [0., ft_complex(2,2), 0.],
   [0., ft_complex(2,2), 2.],
   ])
   print(u.inverse())

   

if __name__ == '__main__':
    main()