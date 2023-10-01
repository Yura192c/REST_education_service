# REST_education_service
Тестовое задание HardQode

# Запуск проекта
***
### Подготовка виртуального окружения
```
python -m venv venv ---create venv
source venv/bin/activate  
pip install -r requirements.txt
```
### Запуск проекта
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```