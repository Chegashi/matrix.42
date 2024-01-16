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
        v2 = Vector([0, 0])
        v1.add(v2)
        print(f'[0, 0] + [0, 0] = \n{v1} \n')

        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        v1.add(v2)
        print(f'[1, 0] + [0, 1] = \n{v1} \n')

        v1 = Vector([1, 1])
        v2 = Vector([1, 1])
        v1.add(v2)
        print(f'[1, 1] + [1, 1] = \n{v1} \n')

        v1 = Vector([21, 21])
        v2 = Vector([21, 21])
        v1.add(v2)
        print(f'[21, 21] + [21, 21] = \n{v1} \n')

        v1 = Vector([-21, 21])
        v2 = Vector([21, -21])
        v1.add(v2)
        print(f'[-21, 21] + [21, -21] = \n{v1} \n')

        v1 = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        v1.add(v2)
        print(f'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] = \n{v1} \n')

        print('\033[31m--Vector part (addition) ERROR-- \033[0m')        

        v1 = Vector([-21, 21])
        v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        try:
                v1.add(v2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[-21, 21] + [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] \n')

        print('\033[32mMatrix part (addition)\033[0m')
        m1 = Matrix([[0, 0], [0, 0]])
        m2 = Matrix([[0, 0], [0, 0]])
        m1.add(m2)
        print(f'[[0, 0], [0, 0]] + [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[1, 0], [0, 1]])
        m2 = Matrix([[0, 0], [0, 0]])
        m1.add(m2)
        print(f'[[1, 0], [0, 1]] + [[0, 0], [0, 0]] = \n{m1}\n')


        m1 = Matrix([[1, 1], [1, 1]])
        m2 = Matrix([[1, 1], [1, 1]])
        m1.add(m2)
        print(f'[[1, 1], [1, 1]] + [[1, 1], [1, 1]] = \n{m1}\n')

        m1 = Matrix([[21, 21], [21, 21]])
        m2 = Matrix([[21, 21], [21, 21]])
        m1.add(m2)
        print(f'[[21, 21], [21, 21]] + [[21, 21], [21, 21]] = \n{m1}\n')

        m1 = Matrix([[21, 21], [21, 21]])
        m2 = Matrix([[0, 0], [0, 0], [21, 21], [21, 21]])

        print('\033[31m-- Matrix part (addition) ERROR-- \033[0m')        
        try:
                m1.add(m2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[[21, 21], [21, 21]] + [[0, 0], [0, 0], [21, 21], [21, 21]] \n')

        print('\033[35mVector part (substract)\033[0m')
        v1 = Vector([0, 0])
        v2 = Vector([0, 0])
        v1.sub(v2)
        print(f'[0, 0] - [0, 0] = \n{v1}\n')

        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        v1.sub(v2)
        print(f'[1, 0] - [0, 1] = \n{v1}\n')

        v1 = Vector([1, 1])
        v2 = Vector([1, 1])
        v1.sub(v2)
        print(f'[1, 1] - [1, 1] = \n{v1}\n')

        v1 = Vector([21, 21])
        v2 = Vector([21, 21])
        v1.sub(v2)
        print(f'[21, 21] - [21, 21] = \n{v1}\n')

        v1 = Vector([-21, 21])
        v2 = Vector([21, -21])
        v1.sub(v2)
        print(f'[-21, 21] - [21, -21] = \n{v1}\n')

        v1 = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        v1.sub(v2)
        print(f'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] = \n{v1}\n')

        print('\033[31m-- VECTOR part (substruction) ERROR-- \033[0m')
        v1 = Vector([-21, 21])
        v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

        try:
                v1.sub(v2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[-21, 21] - [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] \n')

        print('\033[35mMatrix part (substract)\033[0m')
        m1 = Matrix([[0, 0], [0, 0]])
        m2 = Matrix([[0, 0], [0, 0]])
        m1.sub(m2)
        print(f'[[0, 0], [0, 0]] - [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[1, 0], [0, 1]])
        m2 = Matrix([[0, 0], [0, 0]])
        m1.sub(m2)
        print(f'[[1, 0], [0, 1]] - [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[1, 1], [1, 1]])
        m2 = Matrix([[1, 1], [1, 1]])
        m1.sub(m2)
        print(f'[[1, 1], [1, 1]] - [[1, 1], [1, 1]] = \n{m1}\n')

        m1 = Matrix([[21, 21], [21, 21]])
        m2 = Matrix([[21, 21], [21, 21]])
        m1.sub(m2)
        print(f'[[21, 21], [21, 21]] - [[21, 21], [21, 21]] = \n{m1}\n')

        print('\033[31m-- Matrix part (substruction) ERROR-- \033[0m')
        m2 = Matrix([[21, 21], [21, 21]])
        m2 = Matrix([[0, 0], [0, 0], [0, 0], [0, 0]])

        try:
                m1.sub(m2)
        except Exception as e:
                TypeError (f"")
                print(f'ERROR: {e} :[[21, 21], [21, 21]] - [[0, 0], [0, 0], [0, 0], [0, 0]] \n')


        print('\033[34mVector part (multiply with a scalar)\033[0m')
        v1 = Vector([0, 0])
        v1.scl(1)
        print(f'[0, 0] * 1 = \n{v1}\n')

        v1 = Vector([1, 0])
        v1.scl(1)
        print(f'[1, 0] * 1 = \n{v1}\n')

        v1 = Vector([1, 1])
        v1.scl(2)
        print(f'[1, 1] * 2 = \n{v1}\n')

        v1 = Vector([21, 21])
        v1.scl(2)
        print(f'[21, 21] * 2 = \n{v1}\n')

        v1 = Vector([42, 42])
        v1.scl(0.5)
        print(f'[42, 42] * 0.5 = \n{v1}\n')

        print('\033[34mMatrix part (multiply with a scalar)\033[0m')
        m1 = Matrix([[0, 0], [0, 0]])
        m1.scl(0)
        print(f'[[0, 0], [0, 0]] * 0 = \n{m1}\n')

        m1 = Matrix([[1, 0], [0, 1]])
        m1.scl(1)
        print(f'[[1, 0], [0, 1]] * 1 = \n{m1}\n')

        m1 = Matrix([[1, 2], [3, 4]])
        m1.scl(2)
        print(f'[[1, 2], [3, 4]] * 2 = \n{m1}\n')

        m1 = Matrix([[21, 21], [21, 21]])
        m1.scl(0.5)
        print(f'[[21, 21], [21, 21]] * 0.5 = \n{m1}\n')
