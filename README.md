**Запуск на DOCKERe:**

docker-compose up --build

docker-compose exec blog-api bash 

python manage.py migrate

python manage.py createsuperuser

docker-compose up -d 

**Запуск без DOCKERа:**

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

