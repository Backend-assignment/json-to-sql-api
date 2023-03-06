# json-to-sql-api

## objective

This project is a simple API that converts JSON to SQL.

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
