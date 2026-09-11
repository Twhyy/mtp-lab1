"""Консольный интерфейс учебного проекта."""

import argparse

from main import circle_area, greet
from stats import mean, median


def build_parser() -> argparse.ArgumentParser:
    """Собрать разборщик аргументов командной строки."""
    parser = argparse.ArgumentParser(description="Учебная утилита к лабораторной №1")
    sub = parser.add_subparsers(dest="command", required=True)

    hello = sub.add_parser("hello", help="вывести приветствие")
    hello.add_argument("name", help="имя для приветствия")

    area = sub.add_parser("area", help="вычислить площадь круга")
    area.add_argument("radius", type=float, help="радиус круга")

    st = sub.add_parser("stats", help="посчитать среднее и медиану")
    st.add_argument("values", type=float, nargs="+", help="числа через пробел")

    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "hello":
        print(greet(args.name))
    elif args.command == "area":
        print(f"{circle_area(args.radius):.2f}")
    elif args.command == "stats":
        print(f"среднее: {mean(args.values):.2f}, медиана: {median(args.values):.2f}")


if __name__ == "__main__":
    main()
