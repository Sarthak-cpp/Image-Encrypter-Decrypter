from math import pi, cos, sin
def FFT(a, invert):
    n = len(a)
    if n == 1: return
    b = [a[2 * i] for i in range(n // 2)]
    c = [a[2 * i + 1] for i in range(n // 2)]
    FFT(b, invert)
    FFT(c, invert)
    ang = 2 * pi / n * (-1 if invert else 1)
    W = 1
    Wn = cos(ang) + (1j * sin(ang))
    for i in range(n // 2):
        a[i] = b[i] + W * c[i]
        a[i + n // 2] = b[i] - W * c[i]
        if invert:
            a[i] /= 2
            a[i + n // 2] /= 2
        W *= Wn

