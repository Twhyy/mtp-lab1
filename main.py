"""Учебный Python-проект к лабораторной работе №1 по дисциплине
«Методы и технологии программирования» (часть 1)."""

import math


def greet(name: str) -> str:
    """Вернуть приветствие для указанного имени."""
    return f"Привет, {name}!"


def circle_area(radius: float) -> float:
    """Вычислить площадь круга по радиусу."""
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * radius ** 2


def main() -> None:
    print(greet("группа 221141"))
    print(f"Площадь круга радиуса 10: {circle_area(10):.2f}")
    for radius in (1, 2, 3, 4, 5):
        print(f"| r = {radius} | S = {circle_area(radius):8.2f} |")


if __name__ == "__main__":
    main()
