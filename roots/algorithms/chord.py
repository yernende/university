def refine_root(compute_function, limits, digits):
    (a, b) = limits
    epsilon = 1 / 10 ** digits
    i = 0

    while True:
        if i == 0:
            i += 1
        elif i == 1:
            x_previous = x
            i += 1
        elif i == 2:
            if abs(x - x_previous) < epsilon:
                return round(x, digits)
            x_previous = x

        x = (a + b) / 2 - (compute_function(a) + compute_function(b)) / (compute_function(b) - compute_function(a)) * (b - a) / 2
        y = compute_function(x)

        if y == 0:
            return y
        elif y * compute_function(a) < 0:
            b = x
        elif y * compute_function(b) < 0:
            a = x
        else:
            return None
