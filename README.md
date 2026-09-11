# Лабораторная работа №1 — Система контроля версий (Git)

**Федоткин Дмитрий Евгеньевич, группа 221141, вариант 8, лабораторная №1**

Дисциплина «Методы и технологии программирования» (часть 1).

---

## Задания по варианту 8

| Тип | № по общему списку | Формулировка | Раздел |
|-----|--------------------|--------------|--------|
| Средней 1 | 8 | Создать репозиторий на GitHub и связать его с локальным | 1 |
| Средней 2 | 10 | Склонировать чужой репозиторий и изучить историю | 2 |
| Средней 3 | 4 | Изменить файл, сделать второй коммит | 3 |
| Повышенной 1 | 8 | Использовать git submodules | 4 |
| Повышенной 2 | 1 | Разрешить конфликт при слиянии веток | 5 |

Дополнительно, **вне варианта**, в репозитории реализованы Git flow и Pull Request —
см. раздел «Дополнительно».

---

## Структура репозитория

Проект разрабатывается по модели Git flow, поэтому состав файлов зависит от ветки.

Ветка `main` (и `develop`) — то, что видит проверяющий по умолчанию:

```
mtp-lab1/
├── main.py                        # точка входа: приветствие и площади кругов
├── stats.py                       # модуль статистики: mean, median
├── VERSION                        # версия проекта, фиксируется релизной веткой
├── .gitignore                     # игнорируемые файлы Python-проекта
├── .gitmodules                    # описание подключённого сабмодуля
├── libs/
│   └── python-dotenv/             # git submodule -> https://github.com/theskumar/python-dotenv
└── docs/
    ├── conflict-log.md            # разбор конфликта слияния и его разрешения
    └── foreign-repo-history.md    # разбор истории чужого репозитория
```

Только в ветке `feature/cli` (открыт Pull Request №1, в `main` этого файла **нет**):

```
└── cli.py                         # консольный интерфейс на argparse
```

---

## 1. Репозиторий на GitHub и связь с локальным (средняя №8)

Локальный репозиторий создан командой `git init` и связан с репозиторием на GitHub:

```bash
git init -b main
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

Все ветки и теги отправлены на GitHub — вывод `git ls-remote origin`
на момент подготовки релиза 1.1.0:

```
a4ae34fbcf23dfdb787fa4c3c26ef9ff78dda441	HEAD
99ea0cd9f1cb0b27b7596233b8202598813e498b	refs/heads/develop
9c48ece34ed44776ef8a93ce0c28eb11245a8086	refs/heads/feature/cli
bf61bfc907568061c591d660879176667ad2b74c	refs/heads/feature/geometry
6a2cf237643975784e7d9af455a6c30e5fdf51f4	refs/heads/feature/statistics
a4ae34fbcf23dfdb787fa4c3c26ef9ff78dda441	refs/heads/main
a03fb4ae5020d1425fdbef9b99363b1d66ae8caf	refs/heads/release/1.0.0
0e8976033f8160b840c136ee5bf62e860544fece	refs/heads/release/1.0.1
9c48ece34ed44776ef8a93ce0c28eb11245a8086	refs/pull/1/head
8117f42391cbb36b5cb97970823d7d164efacf79	refs/pull/1/merge
4df8f1b7e5e1d18e6070b72e2f674477e8c76c1e	refs/tags/v1.0.0
53a4d33191639f51d5f3c971da581e3946aee26b	refs/tags/v1.0.0^{}
422d7a9453f802ca1d8bdc07dbb2963cf138c7b3	refs/tags/v1.0.1
a4ae34fbcf23dfdb787fa4c3c26ef9ff78dda441	refs/tags/v1.0.1^{}
```

---

## 2. Клонирование чужого репозитория и разбор истории (средняя №10)

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

## 3. Изменение файла и второй коммит (средняя №4)

Файл `main.py` создан самым первым коммитом репозитория, а затем изменён отдельным
атомарным коммитом — в него добавлена функция `circle_area()`.

Первые коммиты репозитория:

```
bf61bfc feat: добавить функцию circle_area для расчёта площади круга
6a2cf23 feat: добавить модуль stats с функциями mean и median
3809164 merge: влить feature/geometry в develop
```

Изменение файла вторым коммитом подтверждается статусом `M` в списке файлов коммита:

```
bf61bfc feat: добавить функцию circle_area для расчёта площади круга
M	main.py
```

Diff этого изменения:

```diff
diff --git a/main.py b/main.py
index e2a1b90..cc9185f 100644
--- a/main.py
+++ b/main.py
@@ -1,14 +1,25 @@
 """Учебный Python-проект к лабораторной работе №1 по дисциплине
 «Методы и технологии программирования» (часть 1)."""
 
+import math
+
 
 def greet(name: str) -> str:
     """Вернуть приветствие для указанного имени."""
     return f"Привет, {name}!"
 
 
+def circle_area(radius: float) -> float:
+    """Вычислить площадь круга по радиусу."""
+    if radius < 0:
+        raise ValueError("Радиус не может быть отрицательным")
+    return math.pi * radius ** 2
+
+
 def main() -> None:
     print(greet("Git"))
+    for radius in (1, 3, 5):
+        print(f"Радиус {radius} -> площадь {circle_area(radius):.2f}")
 
 
 if __name__ == "__main__":
```

---

## 4. Git submodule (повышенная №8)

Внешняя библиотека подключена **именно через `git submodule add`**, а не копированием
файлов. Сабмодуль добавлен в ветке `feature/vendor` и влит в `develop`:

```bash
git checkout -b feature/vendor develop
git submodule add https://github.com/theskumar/python-dotenv.git libs/python-dotenv
git add .gitmodules libs/python-dotenv
git commit -m "feat: подключить python-dotenv как git submodule в libs/"
git checkout develop
git merge --no-ff feature/vendor -m "merge: влить feature/vendor с сабмодулем в develop"
```

**Что подключено:** `python-dotenv` — библиотека чтения переменных окружения из
файла `.env`; по смыслу дополняет правило `.env` в `.gitignore`.

Файл `.gitmodules`, добавленный коммитом `7b09dc7`:

```ini
[submodule "libs/python-dotenv"]
	path = libs/python-dotenv
	url = https://github.com/theskumar/python-dotenv.git
```

Состояние сабмодуля (`git submodule status`):

```
a00cb2eed0704cd6d2071b2004c37e95ccc86ee5 libs/python-dotenv (v1.2.3-2-ga00cb2e)
```

В дереве репозитория сабмодуль записан не как набор файлов, а как **gitlink** —
ссылка на конкретный коммит чужого репозитория (режим `160000`):

```
160000 commit a00cb2eed0704cd6d2071b2004c37e95ccc86ee5	libs/python-dotenv
```

Клонирование этого репозитория вместе с сабмодулем:

```bash
git clone --recurse-submodules https://github.com/Twhyy/mtp-lab1.git
# либо, если репозиторий уже склонирован:
git submodule update --init --recursive
```

---

## 5. Разрешение конфликта при слиянии веток (повышенная №1)

От ветки `develop` отведены две ветки, независимо переписавшие **одни и те же строки**
тела функции `main()` в файле `main.py`:

| Ветка | Что сделала с `main()` |
|-------|------------------------|
| `feature/report-short` | краткий вывод: приветствие «студент» и площадь одного круга радиуса 10 |
| `feature/report-table` | табличный вывод: приветствие «группа 221141» и таблица площадей для радиусов 1-5 |

Первая ветка влилась в `develop` чисто. При слиянии второй Git обнаружил, что те же
строки уже изменены, и остановился:

```bash
git merge --no-ff feature/report-table -m "merge: влить feature/report-table в develop"
```

```
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py
Automatic merge failed; fix conflicts and then commit the result.
```

`git status` показывал файл в состоянии `UU` — изменён обеими сторонами.

Конфликтующий фрагмент `main.py`:

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

Выше `=======` — версия из `develop` (пришедшая из `feature/report-short`),
ниже — версия из `feature/report-table`.

Конфликт разрешён вручную: ни один вариант не отброшен, оба объединены —
приветствие из `feature/report-table` и оба формата вывода площадей.

```python
def main() -> None:
    print(greet("группа 221141"))
    print(f"Площадь круга радиуса 10: {circle_area(10):.2f}")
    for radius in (1, 2, 3, 4, 5):
        print(f"| r = {radius} | S = {circle_area(radius):8.2f} |")
```

Маркеры `<<<<<<<`, `=======`, `>>>>>>>` удалены полностью, результат зафиксирован:

```bash
git add main.py
git commit -m "merge: разрешить конфликт в main.py при слиянии feature/report-table"
```

Merge-коммит конфликта и его родители:

```
commit 2ef3e94
родители: 9571c2f be8e4f0
сообщение: merge: разрешить конфликт в main.py при слиянии feature/report-table
```

Оба родителя меняли один и тот же файл `main.py`:

```
9571c2f merge: влить feature/report-short в develop

be8e4f0 feat: выводить таблицу площадей для радиусов 1-5
main.py
```

Подробный разбор — в файле [`docs/conflict-log.md`](docs/conflict-log.md).

---

## Дополнительно (вне варианта 8)

### Git flow

Репозиторий ведётся по классической модели ветвления:

| Ветка | Роль |
|-------|------|
| `main` | продакшн-ветка, только выпущенные релизы, каждый помечен тегом |
| `develop` | ветка интеграции |
| `feature/geometry`, `feature/statistics`, `feature/vendor` | завершённые фичи |
| `feature/report-short`, `feature/report-table` | ветки, породившие конфликт слияния |
| `feature/cli` | фича, идущая в `develop` через Pull Request |
| `release/1.0.0`, `release/1.0.1`, `release/1.1.0` | подготовка релизов |

Все слияния сделаны с флагом `--no-ff`. Merge-коммиты репозитория:

```
7e30812 merge: влить feature/vendor с сабмодулем в develop
2ef3e94 merge: разрешить конфликт в main.py при слиянии feature/report-table
9571c2f merge: влить feature/report-short в develop
99ea0cd merge: вернуть изменения релиза 1.0.1 в develop
a4ae34f merge: выпустить релиз 1.0.1 в main
53a4d33 merge: выпустить релиз 1.0.0 в main
39ee966 merge: вернуть изменения релиза 1.0.0 в develop
1a48cef merge: влить feature/statistics в develop
3809164 merge: влить feature/geometry в develop
```

Аннотированные теги релизов:

```
v1.0.1          Релиз 1.0.1: документация лабораторной работы
v1.0.0          Релиз 1.0.0: приветствие, геометрия, статистика
```

### Pull Request

**Pull Request №1:** https://github.com/Twhyy/mtp-lab1/pull/1 — ветка `feature/cli`
в базу `develop`, добавляет `cli.py` (CLI на argparse с подкомандами `hello`,
`area`, `stats`). Подтверждение служебными ссылками GitHub:

```
9c48ece34ed44776ef8a93ce0c28eb11245a8086	refs/pull/1/head
8117f42391cbb36b5cb97970823d7d164efacf79	refs/pull/1/merge
```

---

## История коммитов

Граф на момент этого коммита. После него в историю добавятся только два merge-коммита
релиза 1.1.0 — в `main` и обратно в `develop` — и тег `v1.1.0`:

```
* 2ad5431 (HEAD -> release/1.1.0) chore: поднять версию до 1.1.0
*   7e30812 (develop) merge: влить feature/vendor с сабмодулем в develop
|\  
| * 7b09dc7 (feature/vendor) feat: подключить python-dotenv как git submodule в libs/
|/  
*   2ef3e94 merge: разрешить конфликт в main.py при слиянии feature/report-table
|\  
| * be8e4f0 (feature/report-table) feat: выводить таблицу площадей для радиусов 1-5
* |   9571c2f merge: влить feature/report-short в develop
|\ \  
| |/  
|/|   
| * c73d814 (feature/report-short) feat: выводить площадь одного круга радиуса 10
|/  
*   99ea0cd (origin/develop) merge: вернуть изменения релиза 1.0.1 в develop
|\  
| | *   a4ae34f (tag: v1.0.1, origin/main, main) merge: выпустить релиз 1.0.1 в main
| | |\  
| | |/  
| |/|   
| * | 0e89760 (origin/release/1.0.1, release/1.0.1) chore: поднять версию до 1.0.1
|/ /  
* | d30fd9b docs: описать выполнение заданий варианта 10 в README
| *   53a4d33 (tag: v1.0.0) merge: выпустить релиз 1.0.0 в main
| |\  
| | | * 9c48ece (origin/feature/cli, feature/cli) feat: добавить CLI на argparse с командами hello, area и stats
| |_|/  
|/| |   
* | |   39ee966 merge: вернуть изменения релиза 1.0.0 в develop
|\ \ \  
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
develop
  feature/cli
  feature/geometry
  feature/report-short
  feature/report-table
  feature/statistics
  feature/vendor
  main
  release/1.0.0
  release/1.0.1
* release/1.1.0
  remotes/origin/develop
  remotes/origin/feature/cli
  remotes/origin/feature/geometry
  remotes/origin/feature/statistics
  remotes/origin/main
  remotes/origin/release/1.0.0
  remotes/origin/release/1.0.1
```

---

## Как запустить

```bash
python main.py                    # приветствие и площади кругов
```

Из ветки `feature/cli` дополнительно доступен CLI:

```bash
python cli.py hello Дмитрий
python cli.py area 3
python cli.py stats 1 2 3 4 10
```
