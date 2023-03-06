# json-to-sql-api

## objective

This project is a simple API that converts JSON to SQL.

1. create environment

```bash
python -m venv env
```

2. activate environment

windows:
```bash
env\Scripts\activate
```

linux:
```bash
source env/bin/activate
```

3. install requirements

```bash
pip install -r requirements.txt
```

4. startproject

```bash
django-admin startproject core .
```

5. runserver

```bash
python manage.py runserver
```

5. migrate

```bash
python manage.py migrate
```

6. createsuperuser

```bash
python manage.py createsuperuser
```

7. startapp

```bash

python manage.py startapp api
```

8. add app to settings.py

```python
INSTALLED_APPS = [
    'api.apps.ApiConfig',
]
```

9. api models

```python
from django.db import models

class Smartphones(models.Model):
    price = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```

10. add api models to admin.py

```python
from django.contrib import admin
from .models import Smartphones

admin.site.register(Smartphones)
```

11. make migrations

```bash
python manage.py makemigrations
```

12. migrate

```bash
python manage.py migrate
```


## json structure

The JSON structure is as follows:

```json
{
    "apple": {
        "1": {
            "price": "14 299 000 so'm",
            "img_url": "https://assets.asaxiy.uz/product/items/desktop/2b44928ae11fb9384c4cf38708677c482022091716063124908j3O8hyVfPs.jpg.webp",
            "color": "Purple",
            "ram": "6",
            "memory": "128",
            "name": "iPhone 14 Pro",
            "model": "Apple"
        }
    "samsumg": {
        "1": {
            "price": "14 299 000 so'm",
            "img_url": "https://assets.asaxiy.uz/product/items/desktop/2b44928ae11fb9384c4cf38708677c482022091716063124908j3O8hyVfPs.jpg.webp",
            "color": "Purple",
            "ram": "6",
            "memory": "128",
            "name": "iPhone 14 Pro",
            "model": "Apple"
        }
    }
}
```

## sql structure

- Smartphones table

| column name | data type |
| ----------- | --------- |
| id          | int       |
| price       | varchar   |
| img_url     | varchar   |
| color       | varchar   |
| ram         | varchar   |
| memory      | varchar   |
| name       | varchar   |
| model       | varchar   |


## endpoints

| method | endpoint | description |
| ------ | -------- | ----------- |
| POST   | /api/add | adds product to sql database |
| GET   | /api/get/<id> | gets product by id from sql database |
| GET   | /api/get/all | gets all products from sql database |
| DELETE   | /api/delete/<id> | deletes product by id from sql database |
| PUT   | /api/update/<id> | updates product by id from sql database |


## startproject

```bash
python manage.py startproject core .
```

## startapp

```bash
python manage.py startapp api
```
