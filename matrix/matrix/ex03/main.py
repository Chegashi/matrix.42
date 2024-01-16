#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex

def main():
    print("Vector([0, 0]).dot(Vector([0, 0]))")
    print( Vector([0, 0]).dot(Vector([0, 0])))
    print('_______________________________________')

    print("Vector([1, 0]).dot(Vector([0, 0]))")
    print( Vector([1, 0]).dot(Vector([0, 0])))
    print('_______________________________________')

    print("Vector([1, 0]).dot(Vector([1, 0]))")
    print( Vector([1, 0]).dot(Vector([1, 0])))
    print('_______________________________________')
    
    print("Vector([1, 0]).dot(Vector([0, 1]))")
    print( Vector([1, 0]).dot(Vector([0, 1])))
    print('_______________________________________')

    print("Vector([1, 1]).dot(Vector([1, 1]))")
    print( Vector([1, 1]).dot(Vector([1, 1])))
    print('_______________________________________')

    print("Vector([4, 2]).dot(Vector([2, 1]))")
    print( Vector([4, 2]).dot(Vector([2, 1])))
    print('_______________________________________')

if __name__ == '__main__':
    main()
