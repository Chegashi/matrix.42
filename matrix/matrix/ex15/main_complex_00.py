#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

if __name__ == '__main__':
        print("_________________________ [ADITION] _________________________")
        print('\033[32mVector part (addition)\033[0m')
        v1 = Vector([0, 0])
        v2 = Vector([0, ft_complex(0, 0)])
        v1.add(v2)
        print(f'[0, 0] + [0, 0] = \n{v1} \n')

        v1 = Vector([ft_complex(1, 1), 0])
        v2 = Vector([0, ft_complex(1, 1)])
        v1.add(v2)
        print(f'[1+i, 0] + [0, 1+i] = \n{v1} \n')

        v1 = Vector([ft_complex(1, 0), ft_complex(1, 0)])
        v2 = Vector([ft_complex(0, 1), ft_complex(0, 1)])
        v1.add(v2)
        print(f'[1, 1] + [i, i] = \n{v1} \n')

        v1 = Vector([21, 21])
        v2 = Vector([ft_complex(21), ft_complex(1, 21)])
        v1.add(v2)
        print(f'[21, 21] + [21, 1 + 21i] = \n{v1} \n')

        v1 = Vector([ft_complex(-21, 1), ft_complex(21, 21)])
        v2 = Vector([ft_complex(21, 1),  ft_complex(-21, 21)])
        v1.add(v2)
        print(f'[-21 + i, 21 + 21i] + [21 + i, -21 + 21i] = \n{v1} \n')

        v1 = Vector([0, ft_complex(1, 1), 2, ft_complex(3,1), 4, ft_complex(0,5), 6, ft_complex(7), 8, 9])
        v2 = Vector([9, ft_complex(1, 8), 7, ft_complex(6,1), 5, ft_complex(0,4), 3, ft_complex(2), 1, 0])
        v1.add(v2)
        print(f'[0, 1 + i, 2, 3 + i, 4, 5i, 6, 7, 8, 9] + [9, 1 + 8i, 7, 6 + i, 5, 4i, 3, 2, 1, 0] = \n{v1} \n')

        print('\033[31m--Vector part (addition) ERROR-- \033[0m')        

        v1 = Vector([ft_complex(1, -21), ft_complex(21)])
        v2 = Vector([9, 8, ft_complex(7), 6, 5, 4, ft_complex(3,3), 2, 1, 0])

        try:
                v1.add(v2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[1 - 21i, 21] + [9, 8, 7, 6, 5, 4, 3 + 3i, 2, 1, 0] \n')

        print('\033[32mMatrix part (addition)\033[0m')
        m1 = Matrix([[ft_complex(0), ft_complex(0)], [ft_complex(0), 0]])
        m2 = Matrix([[ft_complex(0), ft_complex(0)], [ft_complex(0), 0]])
        m1.add(m2)
        print(f'[[0, 0], [0, 0]] + [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(1), ft_complex(0, 1)], [0, 1]])
        m2 = Matrix([[ft_complex(0), ft_complex(0, 1)], [0, 0]])
        m1.add(m2)
        print(f'[[1, i], [0, 1]] + [[0, i], [0, 0]] = \n{m1}\n')


        m1 = Matrix([[ft_complex(1,1), 1], [ft_complex(1,1), 1]])
        m2 = Matrix([[ft_complex(1,1), 1], [ft_complex(1,1), 1]])
        m1.add(m2)
        print(f'[[1+i, 1], [1+i, 1]] + [[1+i, 1], [1+i, 1]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(21), 21], [ft_complex(0,21), 21]])
        m2 = Matrix([[ft_complex(21), 21], [ft_complex(0,21), 21]])
        m1.add(m2)
        print(f'[[21, 21], [21i, 21]] + [[21, 21], [21i, 21]] = \n{m1}\n')

        m1 = Matrix([[21, 21], [21, ft_complex(21,21)]])
        m2 = Matrix([[ft_complex(0), 0], [0, 0], [21, 21], [21, 21]])

        print('\033[31m-- Matrix part (addition) ERROR-- \033[0m')        
        try:
                m1.add(m2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[[21, 21], [21, 21 + 21i]] + [[0, 0], [0, 0], [21, 21], [21, 21]] \n')

        print('\033[35mVector part (substract)\033[0m')
        v1 = Vector([0, ft_complex(0)])
        v2 = Vector([0, ft_complex(0)])
        v1.sub(v2)
        print(f'[0, 0] - [0, 0] = \n{v1}\n')

        v1 = Vector([1, ft_complex(0)])
        v2 = Vector([0, ft_complex(1)])
        v1.sub(v2)
        print(f'[1, 0] - [0, 1] = \n{v1}\n')

        v1 = Vector([ft_complex(1,1), ft_complex(1, 1)])
        v2 = Vector([ft_complex(1,1), ft_complex(1, 1)])
        v1.sub(v2)
        print(f'[1 + i, 1 + i] - [1 + i, 1 + i] = \n{v1}\n')

        v1 = Vector([ft_complex(21, 1), ft_complex(21,21)])
        v2 = Vector([ft_complex(21, 1), ft_complex(21,21)])
        v1.sub(v2)
        print(f'[21 + i, 21 + 21i] - [21 + i, 21 + 21i] = \n{v1}\n')

        v1 = Vector([ft_complex(1,-21), ft_complex( 21, 1)])
        v2 = Vector([ft_complex(21), ft_complex(-21, 1)])
        v1.sub(v2)
        print(f'[1 - 21i, 21 + i] - [21, -21 + i] = \n{v1}\n')

        v1 = Vector([0, 1, 2, ft_complex(3), ft_complex(0, 4), ft_complex(5,5), 6, 7, 8, 9])
        v2 = Vector([9, 8, 7, ft_complex(6), ft_complex(0, 5), ft_complex(4,4), 3, 2, 1, 0])
        v1.sub(v2)
        print(f'[0, 1, 2, 3, 4i, 5 + 5i, 6, 7, 8, 9] - [9, 8, 7, 6, 5i, 4 + 4i, 3, 2, 1, 0] = \n{v1}\n')

        print('\033[31m-- VECTOR part (substruction) ERROR-- \033[0m')
        v1 = Vector([-21, ft_complex(21, 21)])
        v2 = Vector([9, 8, 7, 6, 5, 4, 3, ft_complex(2), 1, 0])

        try:
                v1.sub(v2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[-21, 21 + 21i] - [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] \n')

        print('\033[35mMatrix part (substract)\033[0m')
        m1 = Matrix([[0, ft_complex(0)], [0, 0]])
        m2 = Matrix([[0, ft_complex(0)], [0, 0]])
        m1.sub(m2)
        print(f'[[0, 0], [0, 0]] - [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(1), 0], [0, ft_complex(1)]])
        m2 = Matrix([[ft_complex(0), 0], [0, ft_complex(0)]])
        m1.sub(m2)
        print(f'[[1, 0], [0, 1]] - [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(1,1), ft_complex(1, 1)], [ft_complex(1,1), ft_complex(1, 1)]])
        m2 = Matrix([[ft_complex(1,1), ft_complex(1, 1)], [ft_complex(1,1), ft_complex(1, 1)]])
        m1.sub(m2)
        print(f'[[1 + i, 1 + i], [1 + i, 1 + i]] - [[1 + i, 1 + i], [1 + i, 1 + i]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(21, 1), ft_complex(0, 21)], [ft_complex(21, 1), ft_complex(21)]])
        m2 = Matrix([[ft_complex(21, 1), ft_complex(0, 21)], [ft_complex(21, 1), ft_complex(21)]])
        m1.sub(m2)
        print(f'[[21, 21], [21, 21]] - [[21, 21], [21, 21]] = \n{m1}\n')

        print('\033[31m-- Matrix part (substruction) ERROR-- \033[0m')
        m2 = Matrix([[21, 21], [21, ft_complex(21, 21)]])
        m2 = Matrix([[0, 0], [0, ft_complex(0)], [0, 0], [0, 0]])

        try:
                m1.sub(m2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[[21 , 21], [21, 21 + 21i]] - [[0, 0], [0, 0], [0, 0], [0, 0]] \n')


        print('\033[34mVector part (multiply with a scalar)\033[0m')
        v1 = Vector([ft_complex(0), ft_complex(0)])
        v1.scl(1)
        print(f'[0, 0] * 1 = \n{v1}\n')

        v1 = Vector([ft_complex(1), 0])
        v1.scl(ft_complex(1))
        print(f'[1, 0] * 1 = \n{v1}\n')

        v1 = Vector([ft_complex(1), ft_complex(1,1)])
        v1.scl(ft_complex(0, 2))
        print(f'[1, 1 + i] * 2i = \n{v1}\n')

        v1 = Vector([21, 21])
        v1.scl(ft_complex(2,2))
        print(f'[21, 21] * (2 + 2i) = \n{v1}\n')

        v1 = Vector([ft_complex(13,42), ft_complex(42,13)])
        v1.scl(ft_complex(13, 37))
        print(f'[13 + 42i, 42 + 13i] * (13 + 37 i) = \n{v1}\n')

        print('\033[34mMatrix part (multiply with a scalar)\033[0m')
        m1 = Matrix([[0, 0], [0, 0]])
        m1.scl(ft_complex(0, 0))
        print(f'[[0, 0], [0, 0]] * 0 = \n{m1}\n')

        m1 = Matrix([[1, 0], [0, 1]])
        m1.scl(ft_complex(1, 1))
        print(f'[[1, 0], [0, 1]] * (1 + i) = \n{m1}\n')

        m1 = Matrix([[1, ft_complex(2, 1)], [ft_complex(3,3), 4]])
        m1.scl(ft_complex(2,1))
        print(f'[[1, 2 + i], [3 + 3i, 4]] * (2 + i) = \n{m1}\n')

        m1 = Matrix([[21, 21], [21, 21]])
        m1.scl(ft_complex(0.5, 0.5))
        print(f'[[21, 21], [21, 21]] * (0.5 + 0.5i) = \n{m1}\n')
