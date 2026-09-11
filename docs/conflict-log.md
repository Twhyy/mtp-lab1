# Разрешение конфликтов при слиянии веток

**Задание повышенной сложности №1** (вариант 8): разрешить конфликт при слиянии веток.

## Конфликт №1 — файл `main.py`

### Откуда взялся конфликт

От ветки `develop` отведены две ветки, которые независимо переписали **одни и те же
строки** тела функции `main()` в файле `main.py`:

| Ветка | Что сделала с `main()` |
|-------|------------------------|
| `feature/report-short` | краткий вывод: приветствие «студент» и площадь одного круга радиуса 10 |
| `feature/report-table` | табличный вывод: приветствие «группа 221141» и таблица площадей для радиусов 1-5 |

Первая ветка влита в `develop` без конфликта. При слиянии второй Git обнаружил,
что те же строки уже изменены, и остановился.

## Команда слияния и сообщение Git

```bash
git merge --no-ff feature/report-table -m "merge: влить feature/report-table в develop"
```

```
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py
Automatic merge failed; fix conflicts and then commit the result.
```

`git status` в этот момент показывал файл в состоянии `UU` (unmerged, обе стороны изменены):

```
UU main.py
```

## Конфликтующий фрагмент `main.py`

```python
<<<<<<< HEAD
    print(greet("студент"))
    print(f"Площадь круга радиуса 10: {circle_area(10):.2f}")
=======
    print(greet("группа 221141"))
    for radius in (1, 2, 3, 4, 5):
        print(f"| r = {radius} | S = {circle_area(radius):8.2f} |")
>>>>>>> feature/report-table
```

Выше маркера `=======` — версия из `develop` (то есть из `feature/report-short`),
ниже — версия из `feature/report-table`.

## Как конфликт разрешён

Ни один из вариантов не отброшен — оба объединены вручную: сохранено приветствие
из `feature/report-table` и оба формата вывода площадей.

```python
def main() -> None:
    print(greet("группа 221141"))
    print(f"Площадь круга радиуса 10: {circle_area(10):.2f}")
    for radius in (1, 2, 3, 4, 5):
        print(f"| r = {radius} | S = {circle_area(radius):8.2f} |")
```

Маркеры `<<<<<<<`, `=======` и `>>>>>>>` удалены полностью, после чего результат
зафиксирован:

```bash
git add main.py
git commit -m "merge: разрешить конфликт в main.py при слиянии feature/report-table"
```


---

## Конфликт №2 — файл `stats.py`

Второй конфликт устроен так, что **обе сливаемые стороны — обычные коммиты**
(не merge-коммиты), и обе меняют один и тот же файл `stats.py`. Это видно
напрямую в `git show --name-only` для каждого родителя.

| Ветка | Коммит | Что сделала с `mean()` |
|-------|--------|------------------------|
| `feature/stats-precision` | `6a3bdb3` | округление результата до четырёх знаков |
| `feature/stats-fsum` | `17662f7` | точное суммирование через `math.fsum` |

Оба коммита правят одни и те же строки тела функции `mean()`.

### Слияние и конфликт

```bash
git checkout feature/stats-precision
git merge --no-ff feature/stats-fsum -m "merge: влить feature/stats-fsum в feature/stats-precision"
```

```
Auto-merging stats.py
CONFLICT (content): Merge conflict in stats.py
Automatic merge failed; fix conflicts and then commit the result.
```

### Версия из `feature/stats-precision`

```python
def mean(values: list[float]) -> float:
    """Среднее арифметическое, округлённое до четырёх знаков."""
    if not values:
        raise ValueError("Последовательность не должна быть пустой")
    return round(sum(values) / len(values), 4)
```

### Версия из `feature/stats-fsum`

```python
def mean(values: list[float]) -> float:
    """Среднее арифметическое с точным суммированием math.fsum."""
    if not values:
        raise ValueError("Последовательность не должна быть пустой")
    return math.fsum(values) / len(values)
```

### Как разрешён

Взято лучшее из обеих веток: точное суммирование `math.fsum` **и** округление
до четырёх знаков.

```python
def mean(values: list[float]) -> float:
    """Среднее арифметическое: точное суммирование math.fsum, округление до 4 знаков."""
    if not values:
        raise ValueError("Последовательность не должна быть пустой")
    return round(math.fsum(values) / len(values), 4)
```

Merge-коммит `8aaa836`, оба его родителя — обычные коммиты, оба меняли `stats.py`:

```
6a3bdb3 feat: округлять среднее до четырёх знаков после запятой
stats.py

17662f7 feat: суммировать значения через math.fsum для точности
stats.py
```
