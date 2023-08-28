# Проект «API для Yatube». Python-разработчик (бекенд) (Яндекс.Практикум)

## Описание

API для Yatube представляет собой проект социальной сети в которой реализованы следующие возможности, 
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

## Стек технологий

* Python 3.11,
* Django 4.2,
* DRF,
* JWT + Djoser

## Запуск проекта в dev-режиме

- Клонировать репозиторий и перейти в него в командной строке.
- Установите и активируйте виртуальное окружение c учетом версии Python 3.7 (выбираем python не ниже 3.7):

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

```bash
python -m pip install --upgrade pip
```

- Затем нужно установить все зависимости из файла requirements.txt

```bash
cd yatube_api
```

```bash
pip install -r requirements.txt
```

- Выполняем миграции:

```bash
python manage.py migrate
```

- Создаем суперпользователя:

```bash
python manage.py createsuperuser
```

- Запускаем проект:

```bash
python manage.py runserver
```
