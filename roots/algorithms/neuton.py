def refine_root(compute_function, compute_derivative, limits, digits):
    (a, b) = limits
    epsilon = 1 / 10 ** digits
    x_next = a

    while True:
        x_previous = x_next
        x_next = x_previous - compute_function(x_previous) / compute_derivative(x_previous)

        if abs(x_next - x_previous) < epsilon:
            return round(x_next, digits)
