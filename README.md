# Django REST Test

Простой Django-проект для тестирования REST API с использованием Docker или локальной среды.

## 📦 Требования

- Python 3+
- Docker и Docker Compose (опционально)

## 🚀 Запуск проекта

### Вариант 1: С использованием Docker

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/kanyebek/djangoresttest.git
   cd djangoresttest
   ```

2. **Постройте и запустите контейнеры:**

   ```bash
   docker-compose up --build
   ```

3. **Примените миграции и создайте суперпользователя (опционально):**

   В новом терминале выполните:

   ```bash
   docker-compose exec blog-api bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Откройте приложение:**

   [http://localhost:8000](http://localhost:8000)

---

### Вариант 2: Без использования Docker

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/kanyebek/djangoresttest.git
   cd djangoresttest
   ```

2. **Создайте и активируйте виртуальное окружение:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции и создайте суперпользователя:**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Запустите сервер разработки:**

   ```bash
   python manage.py runserver
   ```

6. **Откройте приложение:**

   [http://localhost:8000](http://localhost:8000)

---


## 📁 Структура проекта

- `blog/` — приложение блога
- `users/` — приложение пользователей
- `posts/` — приложение постов
- `manage.py` — утилита управления проектом
- `requirements.txt` — зависимости проекта
- `docker-compose.yml` — конфигурация Docker Compose
- `Dockerfile` — инструкция сборки Docker-образа

---

## 🛠️ Полезные команды

- Создание миграций:

  ```bash
  python manage.py makemigrations
  ```

- Применение миграций:

  ```bash
  python manage.py migrate
  ```

- Создание суперпользователя:

  ```bash
  python manage.py createsuperuser
  ```

- Запуск сервера:
- С Docker

  ```bash
  docker-compose up -d 
  ```
- Без Docker
  
  ```bash 
  python manage.py runserver
  ```

---

## 📄 Лицензия

Этот проект распространяется под лицензией MIT.
