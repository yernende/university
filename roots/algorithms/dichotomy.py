def refine_root(compute_function, limits, digits):
    (a, b) = limits
    epsilon = 1 / 10 ** digits

    while (b - a) > epsilon:
        x_mean = (a + b) / 2
        y_mean = compute_function(x_mean)

        if y_mean == 0:
            return y_mean
        elif y_mean * compute_function(a) < 0:
            b = x_mean
        elif y_mean * compute_function(b) < 0:
            a = x_mean
        else:
            return None

    return round((a + b) / 2, digits)
