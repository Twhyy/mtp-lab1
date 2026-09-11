# Разрешение конфликта при слиянии веток

**Задание повышенной сложности №1** (вариант 8): разрешить конфликт при слиянии веток.

## Откуда взялся конфликт

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
