import math

f = lambda x: math.pow(x, 3) - 1 - math.cos(x)

def bisect (func, range_min, range_max, max_delta):
    y1 = func(range_min)
    y2 = func(range_max)

    if y1 == 0:
        return range_min, 0, 0, 0
    elif y2 == 0:
        return range_max, 0, 0, 0

    # both are positive or negative together
    if y1 * y2 > 0:
        return None

    i = 0

    error = math.fabs(range_max - range_min)
    while error > max_delta:
        range_mid = (range_min + range_max) / 2
        y = func(range_mid)


        if y == 0:
            return range_mid, 0, 0, i

        if y2 * y > 0:
            y2 = y
            range_max = range_mid
        else:
            y1 = y
            range_min = range_mid

        i += 1
        error = math.fabs(range_max - range_min)

    z = (range_min + range_max) / 2
    y = func(z)
    return z, error, i

def regula_falsi(func, range_min, range_max, max_delta):
    y1 = func(range_min)
    y2 = func(range_max)

    if y1 == 0:
        return range_min, 0, 0, 0
    elif y2 == 0:
        return range_max, 0, 0, 0

    if y1 * y2 > 0:
        return None

    error = math.fabs(range_max - range_min)
    i = 0
    while error > max_delta:
        secant_zero_arg = find_secant_zero_arg(func, range_min, range_max)
        y = func(secant_zero_arg)

        if y == 0:
            return secant_zero_arg, 0, 0, i

        if y2 * y > 0:
            y2 = y
            range_max = secant_zero_arg
        else:
            y1 = y
            range_min = secant_zero_arg

        i += 1
        error = math.fabs(y)

    z = secant_zero_arg
    y = func(z)
    return z, math.fabs((range_max - range_min))/2, i


def find_secant_zero_arg(func, x1, x2):
    y1, y2 = func(x1), func(x2)
    return x2 - y2 * (x2 - x1)/(y2 - y1)

print(bisect(f, -3, 3, 0.0000000001))
print(regula_falsi(f, -3, 3, 0.0000000001))