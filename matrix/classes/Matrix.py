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

    def is_zero(self) -> bool:
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.data: return False
        return True

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


    def dilatation(self,i , _lambda):
        self.data[i] = [ _lambda * m for m in self.data[i] ]

    def transvection(self,i ,j , _lambda):
        for k in range(self.size[1]):
            self.data[i][k] += self.data[j][k] * _lambda

    def exchange(self, i, j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp

    def row_echelon(self):
        m, n, p, i0 = Matrix(self.data), self.size[0], self.size[1], 0
        for j in range(p):
            k = i0
            while k < n and m.data[k][j] == 0:
                k += 1
            if k < n:
                m.exchange(i0, k)
                m.dilatation(i0, 1/m.data[i0][j])
                for i in range(0, n):
                    if i != i0:
                        Lambda = - m.data[i][j]
                        m.transvection(i, i0, Lambda)
                i0 += 1
        return m

    def determinant(self):
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

    def inverse(self):
        d = self.determinant()
        m = self.adj()
        m.scl(1./d)
        return m

    def adj(self):
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

    def rank(self):
        r = self.row_echelon()
        rank = 0
        for l in range(r.size[0]):
            for c in range(r.size[1]):
                if r.data[l][c] != 0:
                    rank += 1
                    break
        return rank


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
