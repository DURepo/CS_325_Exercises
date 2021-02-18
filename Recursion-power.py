def pow(x, n):
    if n == 1:
        return x

    if n != 1:
        return x * pow(x, n - 1)
