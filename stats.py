"""Простые статистические функции для учебного проекта."""


def mean(values: list[float]) -> float:
    """Среднее арифметическое, округлённое до четырёх знаков."""
    if not values:
        raise ValueError("Последовательность не должна быть пустой")
    return round(sum(values) / len(values), 4)


def median(values: list[float]) -> float:
    """Медиана последовательности чисел."""
    if not values:
        raise ValueError("Последовательность не должна быть пустой")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2
