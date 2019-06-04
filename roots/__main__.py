import math
from PyInquirer import prompt

from algorithms.dichotomy import refine_root as refine_root_dichotomy
from algorithms.chord import refine_root as refine_root_chord
from algorithms.neuton import refine_root as refine_root_neuton

def compute_function(x):
    return math.sin(x)

def compute_derivative(x):
    return math.cos(x)

def main():
    answers = prompt([
        {
            "name": "algorithm",
            "type": "list",
            "message": "Метод поиска корня",
            "choices": [
                {
                    "name": "метод дихотомии",
                    "value": "dichotomy"
                },
                {
                    "name": "метод хорд",
                    "value": "chord"
                },
                {
                    "name": "метод Ньютона",
                    "value": "neuton"
                }
            ]
        },
        {
            "name": "limit_a",
            "type": "input",
            "message": "Нижний предел отрезка для поиска корня",
            "filter": int,
            "default": "-1"
        },
        {
            "name": "limit_b",
            "type": "input",
            "message": "Верхний предел отрезка для поиска корня",
            "filter": int,
            "default": "1"
        },
        {
            "name": "precise_digits",
            "type": "input",
            "message": "Точный знак после запятой",
            "filter": int,
            "default": "10"
        }
    ])

    limits = (answers["limit_a"], answers["limit_b"])
    digits = answers["precise_digits"]

    if answers["algorithm"] == "dichotomy":
        root = refine_root_dichotomy(compute_function, limits, digits)
    elif answers["algorithm"] == "chord":
        root = refine_root_chord(compute_function, limits, digits)
    elif answers["algorithm"] == "neuton":
        root = refine_root_neuton(compute_function, compute_derivative, limits, digits)

    if root is not None:
        print(f"x = {root:0.{digits}f}")
    else:
        print("нет корня")

if __name__ == "__main__":
    main()
