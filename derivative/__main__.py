import numpy
from matplotlib import pyplot
from PyInquirer import prompt

from algorithms.lagrange import compute as compute_derivative_lagrange
from algorithms.trigonometric import compute as compute_derivative_trigonometric

def compute_function(x_data):
    return numpy.sin(x_data)

def compute_derivative_analytic(x_data, order = 1):
    return numpy.sin(x_data + numpy.pi * order / 2)

def main():
    ANALYTIC_POINTS_AMOUNT = 50
    EXPERIMENTAL_POINTS_AMOUNT = 50
    DERIVATIVE_ORDER = 4

    x_data = numpy.linspace(-numpy.pi, numpy.pi, EXPERIMENTAL_POINTS_AMOUNT)
    y_data = compute_function(x_data)

    x_derivative_analytic = numpy.linspace(-numpy.pi, numpy.pi, ANALYTIC_POINTS_AMOUNT)
    y_derivative_analytic = compute_derivative_analytic(x_derivative_analytic, DERIVATIVE_ORDER)

    x_derivative_numerical = x_data

    answers = prompt([
        {
            "name": "algorithm",
            "type": "list",
            "message": "Выберите алгоритм взятия производной",
            "choices": [
                {
                    "name": "на основе интерполяции полиномами Лагранжа",
                    "value": "lagrange"
                },
                {
                    "name": "на основе интерполяции тригонометрическими полиномами",
                    "value": "trigonometric"
                }
            ]
        }
    ])

    if answers["algorithm"] == "lagrange":
        y_derivative_numerical = compute_derivative_lagrange(x_data, y_data, DERIVATIVE_ORDER)
    elif answers["algorithm"] == "trigonometric":
        y_derivative_numerical = compute_derivative_trigonometric(x_data, y_data, DERIVATIVE_ORDER)

    x_delta = numpy.linspace(-numpy.pi, numpy.pi, EXPERIMENTAL_POINTS_AMOUNT)
    y_delta = compute_derivative_analytic(x_delta, DERIVATIVE_ORDER) - y_derivative_numerical

    pyplot.subplot(3, 1, 1)
    pyplot.plot(x_derivative_analytic, y_derivative_analytic)
    pyplot.title(f"Аналитическая производная sin(x) {DERIVATIVE_ORDER}-го порядка")

    pyplot.subplot(3, 1, 2)
    pyplot.plot(x_derivative_numerical, y_derivative_numerical)
    pyplot.title(f"Численная производная sin(x) {DERIVATIVE_ORDER}-го порядка по {EXPERIMENTAL_POINTS_AMOUNT} точкам")

    pyplot.subplot(3, 1, 3)
    pyplot.plot(x_delta, y_delta)
    pyplot.title("Функция разностей")

    pyplot.tight_layout()
    pyplot.show()

if __name__ == "__main__":
    main()
