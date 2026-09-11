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
    print(greet("Git"))
    for radius in (1, 3, 5):
        print(f"Радиус {radius} -> площадь {circle_area(radius):.2f}")


if __name__ == "__main__":
    main()
