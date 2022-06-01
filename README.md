api_final_yatube
Описание
Это API для социальной сети Yatube, где реализованы следующие возможности, 
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.

Установка
Скопируйте проект на свой компьютер:

git clone https://github.com/LariosDeen/api_final_yatube
Cоздайте и активируйте виртуальное окружение для этого проекта:

python3 -m venv env
source env/bin/activate
Установите зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполните миграции:

python3 manage.py migrate
Перейдите в директорию проекта:

cd yatube_api
Запустите проект:

python3 manage.py runserver

Пользователь аутентифицируется посредвстом JWTAuthentication.
Получите токен.
Отправьте POST запрос на URL:

http://127.0.0.1:8000/api/v1/auth/jwt/create/
Получение публикаций GET запрос:

http://127.0.0.1:8000/api/v1/posts/
Создание публикации POST запрос:

http://127.0.0.1:8000/api/v1/posts/

Получение одной публикации GET запрос:

http://127.0.0.1:8000/api/v1/posts/{id}/
Обновление публикации PUT запрос:

http://127.0.0.1:8000/api/v1/posts/{id}/

Частичное обновление публикации PATHС запрос:

http://127.0.0.1:8000/api/v1/posts/{id}/

Удаление публикации DELETE запрос:

http://127.0.0.1:8000/api/v1/posts/{id}/

В проекте использованы следующие технологии:
Python
Django
Django REST Framework