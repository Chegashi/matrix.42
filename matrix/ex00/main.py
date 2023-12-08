import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

if __name__ == '__main__':
    V_ADD_R =  True
    if V_ADD_R:
        print('\033[32mVector part (addition)\033[0m')
        v1 = Vector([0, 0])
        v2 = Vector([0, 0])
        v1.add(v2)
        print(f'[0, 0] + [0, 0] = {v1} \n')

        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        v1.add(v2)
        print(f'[1, 0] + [0, 1] = {v1} \n')    

        v1 = Vector([1, 1])
        v2 = Vector([1, 1])
        v1.add(v2)
        print(f'[1, 1] + [1, 1] = {v1} \n')


        v1 = Vector([21, 21])
        v2 = Vector([21, 21])
        v1.add(v2)
        print(f'[21, 21] + [21, 21] = {v1} \n')

        v1 = Vector([-21, 21])
        v2 = Vector([21, -21])
        v1.add(v2)
        print(f'[-21, 21] + [21, -21] = {v1} \n')

        v1 = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        v1.add(v2)
        print(f'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] = {v1} \n')

    V_ADD_C =  True
    if V_ADD_C:
        v1 = Vector([1, 0])
        v2 = Vector([0, ft_complex(0, 1)])
        v1.add(v2)
        print(f'[1, 0] + [0, i] = {v1} \n')


        v1 = Vector([ft_complex(0, 1), 1])
        v2 = Vector([1, ft_complex(0, 1)])
        v1.add(v2)
        print(f'[i 1] + [1 i] = {v1} \n')

        v1 = Vector([ft_complex(0, 21), 21])
        v2 = Vector([21, ft_complex(0, 21)])
        v1.add(v2)
        print(f'[21i 21] + [21 21i] = {v1} \n')

        v1 = Vector([-5, ft_complex(0, -3)])
        v2 = Vector([ft_complex(3, 0), -5])
        v1.add(v2)
        print(f'[-5 -3i] + [3 -5] = {v1} \n')

        v1 = Vector([0, ft_complex(1), 2, 3, 4, 5, ft_complex(0, 6), 7, 8, 9])
        v2 = Vector([9, ft_complex(8), 7, 6, 5, 4, ft_complex(0, 3), 2, 1, 0])
        v1.add(v2)
        print(f'[0, 1, 2, 3, 4, 5, 6i, 7, 8, 9] + [0, 1, 2, 3, 4, 5, 6i, 7, 8, 9] = {v1} \n')

    M_ADD_R =  True
    if M_ADD_R:
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

    M_ADD_C =  True
    if M_ADD_C:
        print('\033[32mMatrix part (addition)\033[0m')
        m1 = Matrix([[0, 0], [0, 0]])
        m2 = Matrix([[0, 0], [0, 0]])
        m1.add(m2)
        print(f'[[0, 0], [0, 0]] + [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(1), 0], [0, ft_complex(1)]])
        m2 = Matrix([[0, 0], [0, 0]])
        m1.add(m2)
        print(f'[[1, 0], [0, 1]] + [[0, 0], [0, 0]] = \n{m1}\n')


        m1 = Matrix([[1, ft_complex(1, 1)], [1, 1]])
        m2 = Matrix([[1, 1], [1, ft_complex(1, 1)]])
        m1.add(m2)
        print(f'[[1, 1+i], [1, 1]] + [[1, 1], [1, 1+i]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(21), 21], [ft_complex(21,21), 21]])
        m2 = Matrix([[ft_complex(21,21), 21], [21, ft_complex(21)]])
        m1.add(m2)
        print(f'[[21, 21], [21+21i, 21]] + [[21+21i, 21], [21, 21]] = \n{m1}\n')

    V_SUB_R =  True
    if V_SUB_R: 
        print('\033[35mVector part (substract)\033[0m')
        v1 = Vector([0, 0])
        v2 = Vector([0, 0])
        v1.sub(v2)
        print(f'[0, 0] - [0, 0] = {v1}\n')

        v1 = Vector([1, 0])
        v2 = Vector([0, 1])
        v1.sub(v2)
        print(f'[1, 0] - [0, 1] = {v1}\n')

        v1 = Vector([1, 1])
        v2 = Vector([1, 1])
        v1.sub(v2)
        print(f'[1, 1] - [1, 1] = {v1}\n')

        v1 = Vector([21, 21])
        v2 = Vector([21, 21])
        v1.sub(v2)
        print(f'[21, 21] - [21, 21] = {v1}\n')

        v1 = Vector([-21, 21])
        v2 = Vector([21, -21])
        v1.sub(v2)
        print(f'[-21, 21] - [21, -21] = {v1}\n')

        v1 = Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        v2 = Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        v1.sub(v2)
        print(f'[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] = {v1}\n')

    V_SUB_C =  True
    if V_SUB_C: 
        print('\033[35mVector part (substract)\033[0m')
        v1 = Vector([ft_complex(0), 0])
        v2 = Vector([0, ft_complex(0)])
        v1.sub(v2)
        print(f'[0, 0] - [0, 0] = {v1}\n')

        v1 = Vector([ft_complex(1), 0])
        v2 = Vector([0, ft_complex(1)])
        v1.sub(v2)
        print(f'[1, 0] - [0, 1] = {v1}\n')

        v1 = Vector([ft_complex(1), 1])
        v2 = Vector([1, ft_complex(1)])
        v1.sub(v2)
        print(f'[1, 1] - [1, 1] = {v1}\n')

        v1 = Vector([ft_complex(21, 21), ft_complex(21, -21)])
        v2 = Vector([ft_complex(-21, 1), ft_complex(21, 1)])
        v1.sub(v2)
        print(f'[21 + 21i, 21 + -21i] - [-21 +i, 21+i] = {v1}\n')

        v1 = Vector([ft_complex(0,-21), ft_complex(0,21)])
        v2 = Vector([ft_complex(0,21), ft_complex(-21,0)])
        v1.sub(v2)
        print(f'[-21i, 21i] - [21i, -21] = {v1}\n')

        v1 = Vector([0, 1, ft_complex(2), 3, 4, ft_complex(0,5) , 6, 7, 8, 9])
        v2 = Vector([9, 8, ft_complex(7), 6, 5, ft_complex(0,4) , 3, 2, 1, 0])
        v1.sub(v2)
        print(f'[0, 1, 2, 3, 4, 5i, 6, 7, 8, 9] - [9, 8, 7, 6, 5, 4i, 3, 2, 1, 0] = {v1}\n')

    M_SUB_R =  True
    if M_SUB_R:
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

    M_SUB_C =  True
    if M_SUB_C:
        print('\033[35mMatrix part (substract)\033[0m')
        m1 = Matrix([[0, ft_complex(0)], [0, 0]])
        m2 = Matrix([[0, ft_complex(0)], [0, 0]])
        m1.sub(m2)
        print(f'[[0, 0], [0, 0]] - [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[ft_complex(1), 0], [0, ft_complex(0, 1)]])
        m2 = Matrix([[ft_complex(0), 0], [0, ft_complex(0, 0)]])
        m1.sub(m2)
        print(f'[[1, 0], [0, i]] - [[0, 0], [0, 0]] = \n{m1}\n')

        m1 = Matrix([[1, ft_complex(0, 1)], [ft_complex(1, 1), 1]])
        m2 = Matrix([[1, ft_complex(0, 1)], [ft_complex(1, 1), 1]])
        m1.sub(m2)
        print(f'[[1, i], [1+i, 1]] - [[1, i], [1+i, 1]] = \n{m1}\n')

        m1 = Matrix([[21, ft_complex(21,21)], [ft_complex(21,21), 21]])
        m2 = Matrix([[21, ft_complex(0,21)], [ft_complex(21), 21]])
        m1.sub(m2)
        print(f'[[21, 21+21], [21+21i, 21]] - [[21, 21i], [21, 21]] = \n{m1}\n')

    V_SCL_R =  True
    if V_SCL_R:
        print('\033[34mVector part (multiply with a scalar)\033[0m')
        v1 = Vector([0, 0])
        v1.scl(1)
        print(f'[0, 0] * 1 = {v1}\n')

        v1 = Vector([1, 0])
        v1.scl(1)
        print(f'[1, 0] * 1 = {v1}\n')

        v1 = Vector([1, 1])
        v1.scl(2)
        print(f'[1, 1] * 2 = {v1}\n')

        v1 = Vector([21, 21])
        v1.scl(2)
        print(f'[21, 21] * 2 = {v1}\n')

        v1 = Vector([42, 42])
        v1.scl(0.5)
        print(f'[42, 42] * 0.5 = {v1}\n')

    V_SCL_C =  True
    if V_SCL_C:
        print('\033[34mVector part (multiply with a scalar)\033[0m')
        v1 = Vector([ft_complex(0), 0])
        v1.scl(1)
        print(f'[0, 0] * 1 = {v1}\n')

        v1 = Vector([ft_complex(1, 1), 0])
        v1.scl(1)
        print(f'[1+i, 0] * 1 = {v1}\n')

        v1 = Vector([ft_complex(1,0), ft_complex(0,1)])
        v1.scl(2)
        print(f'[1, i] * 2 = {v1}\n')

        v1 = Vector([ft_complex(21), ft_complex(21, 12)])
        v1.scl(2)
        print(f'[21, 21+12i] * 2 = {v1}\n')

        v1 = Vector([ft_complex(42), ft_complex(0,42)])
        v1.scl(0.5)
        print(f'[42, 42i] * 2 = {v1}\n')

    M_SCL_R =  True
    if M_SCL_R:
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

    M_SCL_C = True
    if M_SCL_C:
        print('\033[34mMatrix part (multiply with a scalar)\033[0m')
        m1 = Matrix([[0, ft_complex(0)], [ft_complex(0), 0]])
        m1.scl(ft_complex(0))
        print(f'[[0, 0], [0, 0]] * 0 = \n{m1}\n')

        m1 = Matrix([[1, 0], [0, 1]])
        m1.scl(ft_complex(0, 1))
        print(f'[[1, 0], [0, 1]] * i = \n{m1}\n')

        m1 = Matrix([[ft_complex(1,1), 2], [3, ft_complex(1,4)]])
        m1.scl(ft_complex(0,2))
        print(f'[[1+i, 2], [3, 1+4i]] * 2i = \n{m1}\n')

        m1 = Matrix([[ft_complex(21,1), 21], [21, ft_complex(1,21)]])
        m1.scl(ft_complex(0.5, 0.5))
        print(f'[[21+i, 21], [21, 1+21i]] * 0.5+0.5i = \n{m1}\n')