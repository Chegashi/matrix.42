#! /dev/env python

from typing import Union

class ft_complex():
    def __init__(self:any, x : float, y : float = 0) -> None:
        self.re = x
        self.img = y

    def __str__(self:any) -> str:
        output = ''
        output += f"{self.re:.3g}" if f"{self.re:.3g}" else ''
        output += '+' if self.re and self.img > 0 else ''
        output += f"{self.img:.3g}" if self.img != 0 and self.img != 1 else ''
        output += 'i' if self.img else ''
        return str(output) if output else '0'

    def __abs__(self):
        return (self.re ** 2 + self.img ** 2) ** 0.5

    def __pow__(self, n):
        z = complex(self.re, self.img) ** n
        return ft_complex(z.real, z.imag)

    def __add__(self:any, c:any) -> 'ft_complex':
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re + c, self.img)
        return ft_complex(self.re + c.re, self.img + c.img)

    def __radd__(self:any, c:any) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re + c, self.img)
        return ft_complex(self.re + c.re, self.img + c.img)

    def __sub__(self:any, c:any) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re - c, self.img)
        return ft_complex(self.re - c.re, self.img - c.img)

    def __rsub__(self:any, c:any) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(c - self.re, self.img)
        return ft_complex(c.re - self.re, c.img - self.img)

    def __mul__(self:any, c:any) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re * c, self.img * c)
        return ft_complex(self.re * c.re - self.img * c.img, self.re * c.img + self.img * c.re)

    def __rmul__(self:any, c:any) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re * c, self.img * c)
        return ft_complex(self.re * c.re - self.img * c.img, self.re * c.img + self.img * c.re)

    def __truediv__(self:any, c:any) -> any:
        if isinstance(c, int) or isinstance(c, float):
            return ft_complex(self.re / c, self.img / c)
        return ft_complex((self.re * c.re + self.img * c.img) / (c.re ** 2 - c.img ** 2),
                          (self.img * c.re - self.re * c.img) / (c.re ** 2 - c.img ** 2))

    def __rtruediv__(self:any, c:any) -> any:
        return ft_complex((c * self.re) / (self.re ** 2 + self.img ** 2),
                          (- c * self.img) / (self.re ** 2 + self.img ** 2))

class Matrix():
    def __init__(self:any, data:any) -> None:
        self.data = data
        self.size = (len(data), len(data[0]))

    def is_zero(self:any) -> bool:
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.data: return False
        return True

    def is_squar(self:any) -> bool:
        return self.size[0] == self.size[1]

    def __str__(self:any) -> str:
        lines = ['[' + ' '.join(list(map(str, line))) + ']' for line in self.data]
        return '[' + ',\n'.join(lines) + ']'

    def add(self:any, m:any):
        if self.size != m.size:
            raise Exception(f"can only add Matrix with the same shape {self.size} != {m.size}")

        tmp = [[self.data[i][j] + m.data[i][j] for j in range(self.size[1])] for i in range(self.size[0])]
        self.data = tmp

    def sub(self:any, m:any) -> None:
        if self.size != m.size:
            raise Exception(f"can only add Matrix with the same shape {self.size} != {m.size}")

        tmp = [[self.data[i][j] - m.data[i][j] for j in range(self.size[1])] for i in range(self.size[0])]
        self.data = tmp

    def scl(self:any, s:any) -> None :
        tmp = [[self.data[i][j] * s for j in range(self.size[1])] for i in range(self.size[0])]
        self.data = tmp

    def mul_mat(self:any, m:any) -> any:
        if self.size[1] != m.size[0]:
            raise Exception(f"the number of columns in the first matrix must be equal to the number of rows in the second matrix{self.size} != {m.size}")

        r = [[0] * m.size[1] for _ in range(self.size[0])]
        for l in range(self.size[0]):
            for c in range(m.size[1]):
                for k in range(self.size[1]):
                    r[l][c] += self.data[l][k] * m.data[k][c]
        return Matrix(r)

    def mul_vec(self:any, m:any) -> any:
        if self.size[1] != m.size[0]:
            raise Exception(f"the number of columns in the matrix must be equal to the number of rows in the vector {self.size} != {m.size}")

        m = Matrix(m.data)
        return self.mul_mat(m)

    def trace(self:any) -> float:
        tr = 0
        for i in range(min(self.size[0], self.size[1])):
            tr += self.data[i][i]
        return tr

    def transpose(self:any) -> any:
        return Matrix([[self.data[l][c] for l in range(self.size[0]) ] for c in range(self.size[1])])


    def dilatation(self:any, i:int, _lambda:any) -> None:
        self.data[i] = [ _lambda * m for m in self.data[i] ]

    def transvection(self:any,i:int ,j:int , _lambda:any) -> None:
        for k in range(self.size[1]):
            self.data[i][k] += self.data[j][k] * _lambda

    def exchange(self:any, i:any, j:any) -> None:
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp

    def row_echelon(self:any) -> any:
        m, n, p, i0 = Matrix(self.data), self.size[0], self.size[1], 0
        for i in range(min(n, p)):
            if m.data[i][i]:
                m.data[i] = [aii / m.data[i][i] for aii in m.data[i]]
                k = i + 1
                while k < n:
                    if m.data[k][i]:
                        new_l = [aki / m.data[k][i] for aki in m.data[k]]
                        m.data[k] = [new_l[l] - m.data[i][l] for l in range(p)]
                    k += 1
                    
        return m

    def determinant(self:any) -> any:
        if self.size !=  (2, 2):
            d = 0
            for i in range(self.size[0]):
                coef = -1 if i % 2 else 1
                T = [row[1:] for row in self.data]
                del T[i]
                d += coef * self.data[i][0] * Matrix(T).determinant()
            return d
        else:
            return self.data[0][0] * self.data[1][1] - self.data[1][0] * self.data[0][1]
    
    def inverse(self:any) -> any:
        d = self.determinant()
        if d != 0:
            if self.size[0] == self.size[1]:
                if self.size[0] >= 2:
                    if self.size[0] == 2:
                        c = self.data
                        m = Matrix([[c[1][1], -c[0][1]],
                               [-c[1][0], c[0][0]]])
                    else:
                        m = self.adj()
                    m.scl(1./d)
                    return m
        TypeError("cannot calculate non matrice caree")

    def adj(self) -> any:
        c = [[0] * self.size[1] for _ in range(self.size[0])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                T = [row[:j] + row[j+1:] for row in self.data]
                T = T[:i] + T[i+1:]
                m = Matrix(T)
                coef = -1 if (i + j)% 2 else 1
                c[i][j] = m.determinant() * coef
                _c = Matrix(c)
        return _c.transpose()

    def rank(self) -> int:
        r = self.row_echelon()
        rank = 0
        for l in range(r.size[0]):
            for c in range(r.size[1]):
                if r.data[l][c] != 0:
                    rank += 1
                    break
        return rank

class Vector(Matrix):
    def __init__(self:any, data:any) -> None:
        if isinstance(data, int):
            data = [0] * data
        super().__init__([[d] for d in data])

    def size(self:any) -> tuple:
        return self.size[1]

    def __str__(self:any) -> str:
        return '\n'.join(['[' + str(vi[0]) + ']' for vi in self.data])

    def len(self:any) -> int:
        return self.size()[1]

    def dot(self:any, u:any) -> int:
        s = 0
        if self.size != u.size:
            raise Exception(f"can only add computes the dot product of two vectors of the same dimension {self.size} != {u.size}")

        for x, y in zip(self.data, u.data):
            s += x[0] * y[0]
        return s

    def norm_0(self:any) -> float:
        return sum([xi[0] ** 2 for xi in self.data])

    def norm_1(self:any) -> float:
        return sum([abs(xi[0]) for xi in self.data])

    def norm(self:any) -> float:
        return (sum([xi[0] ** 2 for xi in self.data])) ** 0.5

    def norm_inf(self:any) -> float:
        return max([abs(xi[0]) for xi in self.data])

    def get_data(self:any) -> float:
        return [v for l in self.data for v in l]



def squar(nbr):
    if isinstance(nbr, int) or isinstance(nbr, float):
        return nbr ** 2
    if isinstance(nbr, ft_complex):
        return nbr