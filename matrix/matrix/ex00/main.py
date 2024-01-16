#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector

def main():
    
    print('\033[32mVector part (addition)\033[0m')
    print("Vector([0, 0]).add(Vector([0, 0]))")
    print( Vector([0, 0]).add(Vector([0, 0])))
    print('_______________________________________')

    print("Vector([1, 0]).add(Vector([0, 1]))")
    print( Vector([1, 0]).add(Vector([0, 1])))
    print('_______________________________________')
    

    print("Vector([1, 1]).add(Vector([1, 1]))")
    print( Vector([1, 1]).add(Vector([1, 1])))
    print('_______________________________________')

    print("Vector([21, 21]).add(Vector([21, 21]))")
    print( Vector([21, 21]).add(Vector([21, 21])))
    print('_______________________________________')

    print("Vector([-21, 21]).add(Vector([21, -21]))")
    print( Vector([-21, 21]).add(Vector([21, -21])))
    print('_______________________________________')

    print("Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).add(Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))")
    print( Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).add(Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])))
    print('_______________________________________')


################################################################################

    print('\033[33mMatrix part (addition)\033[0m')

    print("Matrix([[0, 0], [0, 0]]).add(Matrix([[0, 0], [0, 0]]))")
    print( Matrix([[0, 0], [0, 0]]).add(Matrix([[0, 0], [0, 0]])))
    print('_______________________________________')

    print("Matrix([[0, 0], [0, 0]]).add(Matrix([[0, 0], [0, 0]]))")
    print( Matrix([[1, 0], [0, 1]]).add(Matrix([[0, 0], [0, 0]])))
    print('_______________________________________')

    print("Matrix([[1, 1], [1, 1]]).add(Matrix([[1, 1], [1, 1]]))")
    print( Matrix([[1, 1], [1, 1]]).add(Matrix([[1, 1], [1, 1]])))
    print('_______________________________________')

    print("Matrix([[21, 21], [21, 21]]).add(Matrix([[21, 21], [21, 21]]))")
    print( Matrix([[21, 21], [21, 21]]).add(Matrix([[21, 21], [21, 21]])))
    print('_______________________________________')
    
################################################################################
    
    print('\033[32mVector part (subtract)\033[0m')
    print("Vector([0, 0]).sub(Vector([0, 0]))")
    print( Vector([0, 0]).sub(Vector([0, 0])))
    print('_______________________________________')

    print("Vector([1, 0]).sub(Vector([0, 1]))")
    print( Vector([1, 0]).sub(Vector([0, 1])))
    print('_______________________________________')
    

    print("Vector([1, 1]).sub(Vector([1, 1]))")
    print( Vector([1, 1]).sub(Vector([1, 1])))
    print('_______________________________________')

    print("Vector([21, 21]).sub(Vector([21, 21]))")
    print( Vector([21, 21]).sub(Vector([21, 21])))
    print('_______________________________________')

    print("Vector([-21, 21]).sub(Vector([21, -21]))")
    print( Vector([-21, 21]).sub(Vector([21, -21])))
    print('_______________________________________')

    print("Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).sub(Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))")
    print( Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).sub(Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])))
    print('_______________________________________')


################################################################################

    print('\033[33mMatrix part (subtract)\033[0m')

    print("Matrix([[0, 0], [0, 0]]).sub(Matrix([[0, 0], [0, 0]]))")
    print( Matrix([[0, 0], [0, 0]]).sub(Matrix([[0, 0], [0, 0]])))
    print('_______________________________________')

    print("Matrix([[0, 0], [0, 0]]).sub(Matrix([[0, 0], [0, 0]]))")
    print( Matrix([[1, 0], [0, 1]]).sub(Matrix([[0, 0], [0, 0]])))
    print('_______________________________________')

    print("Matrix([[1, 1], [1, 1]]).sub(Matrix([[1, 1], [1, 1]]))")
    print( Matrix([[1, 1], [1, 1]]).sub(Matrix([[1, 1], [1, 1]])))
    print('_______________________________________')

    print("Matrix([[21, 21], [21, 21]]).sub(Matrix([[21, 21], [21, 21]]))")
    print( Matrix([[21, 21], [21, 21]]).sub(Matrix([[21, 21], [21, 21]])))
    print('_______________________________________')
    
################################################################################
    print('\033[32mVector part (multiply)\033[0m')
    
    print("Vector([0, 0]).scl(1)")
    print( Vector([0, 0]).scl(1))
    print('_______________________________________')

    print("Vector([1, 0]).scl(1)")
    print( Vector([1, 0]).scl(1))
    print('_______________________________________')
    

    print("Vector([1, 1]).scl(2)")
    print( Vector([1, 1]).scl(2))
    print('_______________________________________')

    print("Vector([21, 21]).scl(2)")
    print( Vector([21, 21]).scl(2))
    print('_______________________________________')

    print("Vector([42, 42]).scl(0.5)")
    print( Vector([42, 42]).scl(0.5))
    print('_______________________________________')

    print('\033[33mMatrix part (multiply)\033[0m')

    print("Matrix([[0, 0], [0, 0]]).scl(0)")
    print( Matrix([[0, 0], [0, 0]]).scl(0))
    print('_______________________________________')

    print("Matrix([[0, 0], [0, 0]]).scl(1)")
    print( Matrix([[1, 0], [0, 1]]).scl(1))
    print('_______________________________________')

    print("Matrix([[1, 2], [3, 4]]).scl(2)")
    print( Matrix([[1, 2], [3, 4]]).scl(2))
    print('_______________________________________')

    print("Matrix([[21, 21], [21, 21]]).scl(0.5)")
    print( Matrix([[21, 21], [21, 21]]).scl(0.5))
    print('_______________________________________')
    
    
if __name__ == '__main__':
    main()

