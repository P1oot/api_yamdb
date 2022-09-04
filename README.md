# api_yamdb

## Описание.

Данный проект позволяет делать обзоры и давать оценку различным произведенияя, оставлять комментарии.

## Установка.

Клонировать репозиторий и перейти в него в командной строке:
`git clone git@github.com:P1oot/api_yamdb.git`
`cd api_yamdb`

Cоздать и активировать виртуальное окружение:
`python -m venv venv`
`source venv/bin/activate`

Установить зависимости из файла requirements.txt:
`python -m pip install --upgrade pip`
`pip install -r requirements.txt`

Выполнить миграции:
`python manage.py migrate`

Запустить проект:
`python manage.py runserver`

## Примеры запросов.

"Регистрация нового пользователя": "http://127.0.0.1:8000/api/v1/auth/signup/"
"Получение JWT-токена": "http://127.0.0.1:8000/api/v1/auth/token/"
"Обращение к категориям": "http://127.0.0.1:8000/api/v1/categories/"
"Обращение к жанрам": "http://127.0.0.1:8000/api/v1/genres/"
"Обращение к произведениям": "http://127.0.0.1:8000/api/v1/titles/"
"Обращение к отзывам": "http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/"
"Обращение к комментариям": "http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/"

### Авторы:

**Бердинских Даниил** https://github.com/P1oot
**Крицина Анна** https://github.com/cistellula
**Куликов Андрей** https://github.com/Kulikov1
