import numpy
from itertools import combinations

def compute(x_data, y_data, order=1):
    derivative = numpy.zeros(len(x_data))
    combs = list(combinations(range(0, len(x_data)), order))

    for i in range(0, len(x_data)):
        print(i)
        for j in range(0, len(x_data)):
            lagrange_polynomial_derivative = 0

            for t_values in combs:
                if j in t_values:
                    continue

                accumulation = 1.0

                for k in range(0, len(x_data)):
                    if k == j or k in t_values:
                        continue

                    accumulation *= (x_data[i] - x_data[k])
                    accumulation /= (x_data[j] - x_data[k])

                for k in range(0, order):
                    accumulation /= x_data[j] - x_data[t_values[k]]

                lagrange_polynomial_derivative += accumulation

            derivative[i] += y_data[j] * lagrange_polynomial_derivative

    return numpy.math.factorial(order) * derivative
