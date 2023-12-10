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

    def __truediv__(self, c) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re / c, self.img / c)
        return ft_complex((self.re * c.re + self.img * c.img) / (c.re ** 2 - c.img ** 2),
                          (self.img * c.re - self.re * c.img) / (c.re ** 2 - c.img ** 2))

    def __rtruediv__(self, c) -> any:
        return ft_complex((c * self.re) / (self.re ** 2 - self.img ** 2),
                          (- c * self.img) / self.re ** 2 - self.img ** 2)
        

class Matrix():
    def __init__(self, data) -> None:
        self.data = data
        self.size = (len(data), len(data[0]))
        self._type_ = "Matrix"

    def get_size(self) -> tuple:
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

    def mul_mat(self, m):
        r = [[0] * m.size[1] for _ in range(self.size[0])]
        for l in range(self.size[0]):
            for c in range(m.size[1]):
                for k in range(self.size[1]):
                    r[l][c] += self.data[l][k] * m.data[k][c]
        return Matrix(r)

    def mul_vec(self, v):
        m = Matrix(v.data)
        return self.mul_mat(m)

    def trace(self) -> float:
        tr = 0
        for i in range(min(self.size[0], self.size[1])):
            tr += self.data[i][i]
        return tr

    def transpose(self):
        return Matrix([[self.data[l][c] for l in range(self.size[0]) ] for c in range(self.size[1])])

class Vector(Matrix):
    def __init__(self, data) -> None:
        if isinstance(data, int):
            data = [0] * data
        super().__init__([[d] for d in data])
        self._type_ = "Vectore"

    def size(self) -> tuple:
        return self.size[1]

    def __str__(self) -> str:
        return '\n'.join(['[' + str(vi[0]) + ']' for vi in self.data])

    def reshapeToM(self):
        self._type_ = "Matrix"

    def len(self) -> int:
        return self.size()[1]

    def dot(self, u) -> int:
        s = 0
        for x, y in zip(self.data, u.data):
            s += x[0] * y[0]
        return s

    def norm_0(self) -> float:
        return sum([xi[0] ** 2 for xi in self.data])

    def norm_1(self) -> float:
        return sum([abs(xi[0]) for xi in self.data])

    def norm(self) -> float:
        return (sum([xi[0] ** 2 for xi in self.data])) ** 0.5

    def norm_inf(self) -> float:
        return max([abs(xi[0]) for xi in self.data])

    def get_data(self) -> float:
        return [v for l in self.data for v in l  ]



# z = ft_complex(1,1)
# x = ft_complex(3,3)
# # print(z)

# v2 = Vector([x, z])
# print(v2)