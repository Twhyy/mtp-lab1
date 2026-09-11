# Лабораторная работа №1 — Система контроля версий (Git)

**Федоткин Дмитрий Евгеньевич, группа 221141, вариант 10, лабораторная №1**

Дисциплина «Методы и технологии программирования» (часть 1).

---

## Задания по варианту 10

| Тип | № по общему списку | Формулировка | Раздел |
|-----|--------------------|--------------|--------|
| Средней 1 | 10 | Склонировать чужой репозиторий и изучить историю | 3 |
| Средней 2 | 2 | Создать локальный репозиторий Python-проекта | 1 |
| Средней 3 | 8 | Создать репозиторий на GitHub и связать его с локальным | 2 |
| Повышенной 1 | 10 | Реализовать Git flow для своего проекта | 4 |
| Повышенной 2 | 3 | Создать Pull Request | 5 |

---

## Структура репозитория

```
mtp-lab1/
├── main.py                        # точка входа: приветствие и площадь круга
├── stats.py                       # модуль статистики: mean, median
├── cli.py                         # CLI на argparse (ветка feature/cli, идёт через Pull Request)
├── VERSION                        # версия проекта, зафиксированная релизной веткой
├── .gitignore                     # игнорируемые файлы Python-проекта
└── docs/
    └── foreign-repo-history.md    # разбор истории чужого репозитория
```

---

## 1. Локальный репозиторий Python-проекта (средняя №2)

Репозиторий создан локально командой `git init`, сразу настроены имя и почта автора:

```bash
mkdir mtp-lab1 && cd mtp-lab1
git init -b main
git config user.name "Twhyy"
git config user.email "Dalhimik3@gmail.com"
```

Первые два коммита заложили основу Python-проекта:

```
bf61bfc feat: добавить функцию circle_area для расчёта площади круга
6a2cf23 feat: добавить модуль stats с функциями mean и median
```

Для Python-проекта добавлен `.gitignore`:

```gitignore
# Байт-код и кеш Python
__pycache__/
*.pyc
*.pyo

# Виртуальные окружения
.venv/
venv/

# Переменные окружения
.env

# Служебные файлы IDE
.idea/
.vscode/
```

Проверка, что проект работает:

```bash
$ python main.py
Привет, Git!
Радиус 1 -> площадь 3.14
Радиус 3 -> площадь 28.27
Радиус 5 -> площадь 78.54
```

---

## 2. Репозиторий на GitHub и связь с локальным (средняя №8)

На GitHub создан репозиторий `mtp-lab1`, после чего связан с локальным:

```bash
git remote add origin https://github.com/Twhyy/mtp-lab1.git
git push -u origin main
git push --all && git push --tags
```

**Адрес репозитория:** https://github.com/Twhyy/mtp-lab1

Проверка привязки (`git remote -v`):

```
origin	https://github.com/Twhyy/mtp-lab1.git (fetch)
origin	https://github.com/Twhyy/mtp-lab1.git (push)
```

Все ветки и теги отправлены на GitHub — вывод `git ls-remote origin`:

```
53a4d33191639f51d5f3c971da581e3946aee26b	HEAD
39ee966f36bf6dc2d254b3e77b631bf4b9ca3f5a	refs/heads/develop
9c48ece34ed44776ef8a93ce0c28eb11245a8086	refs/heads/feature/cli
bf61bfc907568061c591d660879176667ad2b74c	refs/heads/feature/geometry
6a2cf237643975784e7d9af455a6c30e5fdf51f4	refs/heads/feature/statistics
53a4d33191639f51d5f3c971da581e3946aee26b	refs/heads/main
a03fb4ae5020d1425fdbef9b99363b1d66ae8caf	refs/heads/release/1.0.0
9c48ece34ed44776ef8a93ce0c28eb11245a8086	refs/pull/1/head
8117f42391cbb36b5cb97970823d7d164efacf79	refs/pull/1/merge
4df8f1b7e5e1d18e6070b72e2f674477e8c76c1e	refs/tags/v1.0.0
53a4d33191639f51d5f3c971da581e3946aee26b	refs/tags/v1.0.0^{}
```

---

## 3. Клонирование чужого репозитория и разбор истории (средняя №10)

**Адрес чужого репозитория:** https://github.com/psf/requests

```bash
git clone https://github.com/psf/requests.git external/requests
```

Клон размещён вне этого репозитория, чтобы чужая история не смешалась с историей
лабораторной работы.

`git log` чужого репозитория (последние 10 коммитов):

```
dae7ef63 Bump https://github.com/astral-sh/ruff-pre-commit (#7616)
5460f467 Update lock-issues.yml to latest dependencies (#7609)
6af0b941 Bump https://github.com/astral-sh/ruff-pre-commit (#7608)
8f8b212d Bump https://github.com/astral-sh/ruff-pre-commit (#7606)
80683562 Bump https://github.com/astral-sh/ruff-pre-commit (#7603)
1f6589ec Bump https://github.com/astral-sh/ruff-pre-commit (#7598)
414f0513 Bump the actions group with 2 updates (#7596)
ded32878 Bump https://github.com/astral-sh/ruff-pre-commit (#7597)
69f84847 Bump the actions group with 3 updates (#7591)
b17c61b6 Bump https://github.com/astral-sh/ruff-pre-commit (#7590)
```

Сводка по истории:

```
всего коммитов : 6494
тегов (релизов): 162
первый коммит  : e7615cbc 2011-02-13 Kenneth Reitz
последний      : dae7ef63 2026-09-02 dependabot[bot]
```

Топ-5 авторов (`git shortlog -sn --all`):

```
  3245	Kenneth Reitz
   656	Cory Benfield
   382	Nate Prewitt
   329	Ian Cordasco
   105	Ian Stapleton Cordasco
```

Полный разбор с графом ветвления, тегами и выводами —
в файле [`docs/foreign-repo-history.md`](docs/foreign-repo-history.md).

---

## 4. Git flow (повышенная №10)

В проекте реализована классическая модель ветвления Git flow.

| Ветка | Роль |
|-------|------|
| `main` | продакшн-ветка, содержит только выпущенные релизы, каждый помечен тегом |
| `develop` | ветка интеграции, куда вливаются завершённые фичи |
| `feature/geometry` | фича: расчёт площади круга |
| `feature/statistics` | фича: модуль статистики `mean` / `median` |
| `feature/cli` | фича: CLI на argparse, вливается в `develop` через Pull Request |
| `release/1.0.0` | подготовка релиза 1.0.0: фиксация версии в файле `VERSION` |
| `release/1.0.1` | подготовка релиза 1.0.1: документация лабораторной работы |

Последовательность команд, реализующая модель:

```bash
# ветка интеграции
git checkout -b develop main

# фича отводится от develop и возвращается в неё слиянием с merge-коммитом
git checkout -b feature/geometry develop
git commit -m "feat: добавить функцию circle_area для расчёта площади круга"
git checkout develop
git merge --no-ff feature/geometry -m "merge: влить feature/geometry в develop"

# релизная ветка стабилизирует версию
git checkout -b release/1.0.0 develop
git commit -m "chore: зафиксировать версию 1.0.0 для релиза"

# релиз уходит в main и помечается аннотированным тегом
git checkout main
git merge --no-ff release/1.0.0 -m "merge: выпустить релиз 1.0.0 в main"
git tag -a v1.0.0 -m "Релиз 1.0.0"

# и возвращается обратно в develop
git checkout develop
git merge --no-ff release/1.0.0 -m "merge: вернуть изменения релиза 1.0.0 в develop"
```

Все слияния выполнены с флагом **`--no-ff`**, поэтому каждое завершение фичи и
каждый релиз оставили в истории отдельный merge-коммит. Merge-коммиты репозитория:

```
39ee966 merge: вернуть изменения релиза 1.0.0 в develop
53a4d33 merge: выпустить релиз 1.0.0 в main
1a48cef merge: влить feature/statistics в develop
3809164 merge: влить feature/geometry в develop
```

Аннотированные теги релизов:

```
v1.0.0          Релиз 1.0.0: приветствие, геометрия, статистика
```

---

## 5. Pull Request (повышенная №3)

Фича `feature/cli` вливается в `develop` не напрямую, а через Pull Request —
как того требует командная работа по Git flow.

**Pull Request №1:** https://github.com/Twhyy/mtp-lab1/pull/1

- база: `develop`
- ветка-источник: `feature/cli`
- содержимое: модуль `cli.py` — консольный интерфейс на `argparse`
  с подкомандами `hello`, `area` и `stats`

Существование Pull Request подтверждается служебными ссылками GitHub
(команда `git ls-remote origin refs/pull/*`):

```
9c48ece34ed44776ef8a93ce0c28eb11245a8086	refs/pull/1/head
8117f42391cbb36b5cb97970823d7d164efacf79	refs/pull/1/merge
```

`refs/pull/1/head` указывает на коммит `9c48ece` — вершину ветки `feature/cli`.

Что делает CLI из этого Pull Request:

```bash
$ python cli.py hello Дмитрий
Привет, Дмитрий!

$ python cli.py area 3
28.27

$ python cli.py stats 1 2 3 4 10
среднее: 4.00, медиана: 3.00
```

---

## История коммитов

Граф на момент подготовки релиза 1.0.1 (слияние этого релиза в `main` и обратно
в `develop` добавит к графу ещё два merge-коммита):

```
* 9c48ece (origin/feature/cli, feature/cli) feat: добавить CLI на argparse с командами hello, area и stats
*   39ee966 (HEAD -> develop, origin/develop) merge: вернуть изменения релиза 1.0.0 в develop
|\  
| | *   53a4d33 (tag: v1.0.0, origin/main, main) merge: выпустить релиз 1.0.0 в main
| | |\  
| | |/  
| |/|   
| * | a03fb4a (origin/release/1.0.0, release/1.0.0) chore: зафиксировать версию 1.0.0 для релиза
|/ /  
* | 9a5efdb docs: добавить отчёт о разборе истории чужого репозитория
* |   1a48cef merge: влить feature/statistics в develop
|\ \  
| * | 6a2cf23 (origin/feature/statistics, feature/statistics) feat: добавить модуль stats с функциями mean и median
|/ /  
* |   3809164 merge: влить feature/geometry в develop
|\ \  
| |/  
|/|   
| * bf61bfc (origin/feature/geometry, feature/geometry) feat: добавить функцию circle_area для расчёта площади круга
|/  
* 1f6f8aa chore: добавить .gitignore для Python-проекта
* 56b44e5 feat: инициализировать Python-проект с функцией приветствия
```

## Ветки

```
* develop
  feature/cli
  feature/geometry
  feature/statistics
  main
  release/1.0.0
  remotes/origin/develop
  remotes/origin/feature/cli
  remotes/origin/feature/geometry
  remotes/origin/feature/statistics
  remotes/origin/main
  remotes/origin/release/1.0.0
```

---

## Как запустить

```bash
python main.py                    # приветствие и площади кругов
python cli.py hello Дмитрий       # CLI: приветствие
python cli.py area 3              # CLI: площадь круга
python cli.py stats 1 2 3 4 10    # CLI: среднее и медиана
```
