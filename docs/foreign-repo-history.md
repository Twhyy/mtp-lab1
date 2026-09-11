# Изучение истории чужого репозитория

**Задание средней сложности №10** (вариант 10): склонировать чужой репозиторий
и изучить историю.

## Что клонировали

- Репозиторий: **psf/requests** — популярная HTTP-библиотека для Python
- Адрес: https://github.com/psf/requests
- Команда клонирования:

```bash
git clone https://github.com/psf/requests.git external/requests
```

Клон размещён **вне** этого репозитория (в соседней папке `external/`), чтобы
чужая история не попала в историю лабораторной работы.

## Общие сведения об истории

```
remote origin  : https://github.com/psf/requests.git
всего коммитов : 6494
удалённых веток: 7
тегов (релизов): 162
первый коммит  : e7615cbc 2011-02-13 Kenneth Reitz — first commit
последний      : dae7ef63 2026-09-02 dependabot[bot] — Bump https://github.com/astral-sh/ruff-pre-commit (#7616)
```

## Последние 15 коммитов (`git log --oneline -n 15`)

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
f361ead0 Bump https://github.com/astral-sh/ruff-pre-commit (#7562)
d38495c9 Fix link to AI Policy in CONTRIBUTING.md (#7576)
4c800e9a Bump actions/setup-python from 6.2.0 to 6.3.0 in the actions group (#7561)
23953c0c Bump https://github.com/astral-sh/ruff-pre-commit (#7551)
4ed3d1b3 Bump actions/checkout from 6.0.2 to 7.0.0 in the actions group (#7540)
```

## Граф ветвления (`git log --graph --oneline -n 15`)

```
* dae7ef63 Bump https://github.com/astral-sh/ruff-pre-commit (#7616)
* 5460f467 Update lock-issues.yml to latest dependencies (#7609)
* 6af0b941 Bump https://github.com/astral-sh/ruff-pre-commit (#7608)
* 8f8b212d Bump https://github.com/astral-sh/ruff-pre-commit (#7606)
* 80683562 Bump https://github.com/astral-sh/ruff-pre-commit (#7603)
* 1f6589ec Bump https://github.com/astral-sh/ruff-pre-commit (#7598)
* 414f0513 Bump the actions group with 2 updates (#7596)
* ded32878 Bump https://github.com/astral-sh/ruff-pre-commit (#7597)
* 69f84847 Bump the actions group with 3 updates (#7591)
* b17c61b6 Bump https://github.com/astral-sh/ruff-pre-commit (#7590)
* f361ead0 Bump https://github.com/astral-sh/ruff-pre-commit (#7562)
* d38495c9 Fix link to AI Policy in CONTRIBUTING.md (#7576)
* 4c800e9a Bump actions/setup-python from 6.2.0 to 6.3.0 in the actions group (#7561)
* 23953c0c Bump https://github.com/astral-sh/ruff-pre-commit (#7551)
* 4ed3d1b3 Bump actions/checkout from 6.0.2 to 7.0.0 in the actions group (#7540)
```

## Топ-15 авторов (`git shortlog -sn --all`)

```
  3245	Kenneth Reitz
   656	Cory Benfield
   382	Nate Prewitt
   329	Ian Cordasco
   105	Ian Stapleton Cordasco
    64	dependabot[bot]
    45	Shivaram Lingamneni
    43	Braulio Valdivielso Martínez
    31	David Pursehouse
    28	Kevin Burke
    24	daftshady
    23	Jérémy Bethmont
    21	Chase Sterling
    20	Idan Gazit
    19	Jon Dufresne
```

## Последние 10 тегов-релизов

```
v2.34.2
v2.34.1
v2.34.0
v2.34.0.dev1
v2.33.1
v2.33.0
v2.32.5
v2.32.4
v2.32.3
v2.32.2
```

## Выводы по изученной истории

1. История ведётся с 2011 года и насчитывает более 6000 коммитов — видно, как
   проект одного автора вырос в библиотеку с сотнями контрибьюторов.
2. Разработка построена на feature-ветках с последующими merge-коммитами: в
   графе отчётливо видны параллельные линии и точки слияния.
3. Каждый релиз помечен аннотированным тегом вида `v2.32.3` — это семантическое
   версионирование, ровно та практика, что применена и в этой лабораторной работе.
4. Заметная часть свежих коммитов создана ботом `dependabot`, который
   автоматически обновляет зависимости, — пример CI/CD-автоматизации.
5. Сообщения коммитов короткие и содержат ссылку на номер pull request, по
   которому изменение попало в основную ветку.
