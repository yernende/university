import numpy

def compute(x_data, y_data, order=1):
    n = len(x_data)

    alpha_vector = numpy.zeros(n)
    beta_vector = numpy.zeros(n)

    for i in range(0, n):
        for j in range(0, n):
            alpha_vector[i] += y_data[j] * numpy.cos((i + 1) * x_data[j])
            beta_vector[i] += y_data[j] * numpy.sin((i + 1) * x_data[j])

    alpha_vector *= (2 / numpy.pi / n)
    beta_vector *= (2 / numpy.pi / n)

    derivative = numpy.zeros(n)

    for i in range(0, n):
        for j in range(0, n):
            derivative[i] += alpha_vector[j] * numpy.cos((j + 1) * x_data[i] + numpy.pi * order / 2)
            derivative[i] += beta_vector[j] * numpy.sin((j + 1) * x_data[i] + numpy.pi * order / 2)

    return derivative
