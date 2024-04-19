def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulo with zero divisor")
    return x % y
