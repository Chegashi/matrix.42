import math

def tan(x):
    return math.sin(x) / math.cos(x)

def fused_multiply_add(a, b, c):
    return a * b + c

def projection(fov, ratio, near, far):
    f = 1.0 / tan(math.radians(fov) / 2.0)
    nf = 1.0 / fused_multiply_add(near, -far, far + near)

    return [
        [f / ratio, 0.0, 0.0, 0.0],
        [0.0, f, 0.0, 0.0],
        [0.0, 0.0, (far + near) * nf, -1.0],
        [0.0, 0.0, fused_multiply_add(2.0 * far * near, nf, 0.0), 0.0]
    ]

def main():
    fov = 60.0
    ratio = 16.0 / 9.0
    near = 0.1
    far = 100.0
    projection_matrix = projection(fov, ratio, near, far)
    for row in projection_matrix:
        print(", ".join(f"{val:.4f}" for val in row))

if __name__ == "__main__":
    main()
