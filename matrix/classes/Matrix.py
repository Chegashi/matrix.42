#! /dev/env python
class ft_complex():
    def __init__(self, x, y=0) -> None:
        self.re = x
        self.img = y

    def __str__(self) -> str:
        output = ''
        output += str(self.re) if self.re else ''
        output += '+' if self.re and self.img > 0 else ''
        output += str(self.img) if self.img != 0 and self.img != 1 else ''
        output += 'i' if self.img else ''
        return output if output else '0'

    def __add__(self, c) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re + c, self.img)
        return ft_complex(self.re + c.re, self.img + c.img)

    def __radd__(self, c) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re + c, self.img)
        return ft_complex(self.re + c.re, self.img + c.img)

    def __sub__(self, c) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re - c, self.img)
        return ft_complex(self.re - c.re, self.img - c.img)

    def __rsub__(self, c) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(c - self.re, self.img)
        return ft_complex(c.re - self.re, c.img - self.img)

    def __mul__(self, c) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re * c, self.img * c)
        return ft_complex(self.re * c.re - self.img * c.img, self.re * c.img + self.img * c.re)

    def __rmul__(self, c) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re * c, self.img * c)
        return ft_complex(self.re * c.re - self.img * c.img, self.re * c.img + self.img * c.re)

class Matrix():

    def __init__(self, data) -> None:
        self.data = data
        self.size = (len(data), len(data[0]))
        self._type_ = "Matrix"

    def size(self) -> tuple:
        return self.size

    def is_squar(self) -> bool:
        return self.size[0] == self.size[1]

    def __str__(self) -> str:
        lines = ['[' + ' '.join(list(map(str, line))) + ']' for line in self.data]
        return '[' + ',\n'.join(lines) + ']'

    def print(self) -> None:
        print(self)

    def reshapeToV(self):
        self._type_ = "Vector"

    def add(self, m):
        tmp = [[self.data[i][j] + m.data[i][j] for j in range(self.size[1])] for i in range(self.size[0])]
        self.data = tmp

    def sub(self, m):
        tmp = [[self.data[i][j] - m.data[i][j] for j in range(self.size[1])] for i in range(self.size[0])]
        self.data = tmp

    def scl(self, s):
        tmp = [[self.data[i][j] * s for j in range(self.size[1])] for i in range(self.size[0])]
        self.data = tmp       

class Vector(Matrix):
    def __init__(self, data) -> None:
        super().__init__([data])
        self._type_ = "Vectore"

    def size(self) -> tuple:
        return super().size()[0]

    def __str__(self) -> str:
        return '[' + ' '.join(list(map(str, self.data[0]))) + ']'

    def reshapeToM(self):
        self._type_ = "Vector"

