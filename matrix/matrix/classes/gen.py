from typing import Union

from Matrix import ft_complex

# class ft_complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

def your_function(value: Union[float, ft_complex]) -> None:
    # Your function implementation here
    print(value)

j = ft_complex(2, 1)
# print(f"A: {j}")
# Examples of using the function
your_function(3.14)  # Pass a float
your_function(j)  # Pass an ft_complex object
