#!/usr/bin/env pyhton

import sys

sys.path.append('../')

from classes.Matrix import Matrix
from classes.Matrix import Vector
from classes.Matrix import ft_complex


def main():
    v1 = Vector([0])
    v2 = Vector([1])
    v3 = Vector([0, 0])
    v4 = Vector([1, 0])
    v5 = Vector([2, 1])
    v6 = Vector([4, 2])
    v7 = Vector([-4, -2])

    print("______ Euclidean norm _______")
    split = "________________"
    print(f"{v1} => {v1.norm()} \n {split}")
    print(f"{v2} => {v2.norm()} \n {split}")
    print(f"{v3} => {v3.norm()} \n {split}")
    print(f"{v4} => {v4.norm()} \n {split}")
    print(f"{v5} => {v5.norm()} \n {split}")
    print(f"{v6} => {v6.norm()} \n {split}")
    print(f"{v7} => {v7.norm()} \n {split}")
    
    
    print("______ Manhattan norm _______")
    print(f"{v1} => {v1.norm_1()} \n {split}")
    print(f"{v2} => {v2.norm_1()} \n {split}")
    print(f"{v3} => {v3.norm_1()} \n {split}")
    print(f"{v4} => {v4.norm_1()} \n {split}")
    print(f"{v5} => {v5.norm_1()} \n {split}")
    print(f"{v6} => {v6.norm_1()} \n {split}")
    print(f"{v7} => {v7.norm_1()} \n {split}")



    print("______ Supremum norm _______")
    split = "________________"
    print(f"{v1} => {v1.norm_inf()} \n {split}")
    print(f"{v2} => {v2.norm_inf()} \n {split}")
    print(f"{v3} => {v3.norm_inf()} \n {split}")
    print(f"{v4} => {v4.norm_inf()} \n {split}")
    print(f"{v5} => {v5.norm_inf()} \n {split}")
    print(f"{v6} => {v6.norm_inf()} \n {split}")


    u = Vector([0., 0., 0.])
    print(f"{u.norm_1()}")
    
    print(f"([0., 0., 0.]")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 0.0, 0.0, 0.0
    
    u = Vector([1., 2., 3.])
    print(f"([1., 2., 3.")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 6.0, 3.74165738, 3.0
    
    u = Vector([-1., -2.])
    print(f"([[-1., -2.]")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")
    # // 3.0, 2.236067977, 2.0

if __name__ == '__main__':
    main()