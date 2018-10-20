# Storage API

Простое АПИ для склада (Django+DRF)

### Installing

Все необходимые пакеты в файле requirements.txt

```
pip install requirements.txt
```

## Running the tests

Для запуска юнит-тестов АПИ-поинтов выполнить:
```
python manage.py test
```

### API points

Описание всех АПИ-поинтов (Swagger)

```
http://localhost:8000
```

Получить список всех товаров
```
/api/
method=GET
```

Получить список всех продавцов
```
/api/sellers/
method=GET
```

Создать товар
```
/api/create/
method=POST
{
  "name": "string",
  "description": "string",
  "seller": seller.id
}
```

Обновить товар. Все поля опциональные
```
/api/update/<item.id>
method=PATCH
{
  "name": "string",
  "description": "string"
}
```

Удалить товар.
```
/api/delete/<item.id>
method=DELETE
```
