# Movie API

RESTful web service to obtain movie information created using Django Restframework

![GitHub top language](https://img.shields.io/github/languages/top/saintlyzero/NestedFetch)
## Postman Documentaion : [link](https://documenter.getpostman.com/view/8879912/SWE3beS5)
![enter image description here](https://icon-library.net/images/postman-icon/postman-icon-6.jpg)

| Module | Method | Desciption | Endpoint | Usage | Access |
|--|--|--|--|--|--|
| User Management | `POST` | Adds new user | http://34.93.43.145:8000/user | [Details](#add-user) | Admin |
| User Management | `DELETE` | Deletes specified user | http://34.93.43.145:8000/user | [Details](#delete-user) | Admin |
| Movie | `POST` | Adds new movie | http://34.93.43.145:8000/movie | [Details](#add-movie) | Admin |
| Movie | `DELETE` | Deletes specified movie | http://34.93.43.145:8000/movie | [Details](#delete-movie) | Admin |
| Movie | `PUT` | Updates specified movie | http://34.93.43.145:8000/movie | [Details](#update-user) | Admin |
| Movie | `GET` | Fetches movie details matching specified keyword | http://34.93.43.145:8000/movie | [Details](#fetch-user) | Admin/Registered User |

## Movie Module

### Add Movie

| Method | Endpoint  | Access |
|--|--|--|
| `POST` | `/movie` | Admin |


#### Case 1 : Valid input with token

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "title":"Justice League",
        "description":"Steppenwolf and his Parademons set out to take over the Earth.",
        "rating":4.3,
        "year":2017
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Added new record",
    "record": {
        "title": "Justice League",
        "id": 25
    }
}
```

#### Case 2 : Valid input with email and password

#### Request

```json
{
    "email":"admin@gmail.com",
    "password":"admin",
    "data": {
        "title":"Justice League",
        "description":"Steppenwolf and his Parademons set out to take over the Earth.",
        "rating":4.3,
        "year":2017
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Added new record",
    "record": {
        "title": "Justice League",
        "id": 25
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im"
}
```

#### Case 3 : Duplicate Record

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "title":"Justice League",
        "description":"Steppenwolf and his Parademons set out to take over the Earth.",
        "rating":4.3,
        "year":2017
    }
}
```

#### Response

```json
{
    "status": 400,
    "result": {
        "title": [
            "movies with this title already exists."
        ]
    },
    "record": {
        "title": "Justice League",
        "id": 25
    }
}
```

#### Case 4 : Invalid credentials

#### Request

```json
{
    "email":"zzzzdmin@gmail.com",
    "password":"admin",
    "data": {
        "title":"Justice League",
        "description":"Steppenwolf and his Parademons set out to take over the Earth.",
        "rating":4.3,
        "year":2017
    }
}
```

#### Response

```json
{
    "status": 401,
    "result": "Invalid Credentials"
}
```

#### Case 5 : Invalid Token

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "title":"Justice League",
        "description":"Steppenwolf and his Parademons set out to take over the Earth.",
        "rating":4.3,
        "year":2017
    }
}
```

#### Response

```json
{
    "status": 401,
    "result": "Invalid Token, please login"
}
```

#### Case 6 : Non - Admin account

#### Request

```json
{
    "email":"jhon@gmail.com",
    "password":"jhon",
    "data": {
        "title":"Justice League",
        "description":"Steppenwolf and his Parademons set out to take over the Earth.",
        "rating":4.3,
        "year":2017
    }
}
```

#### Response

```json
{
    "status": 403,
    "result": "Not Authorized to perform this operation",
}
```

#### Case 7 : Invalid input data

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "title":"Justice League 2",
        "description":"Steppenwolf and his Parademons set out to take over the Earth.",
        "rating":14.3,
        "year":20127
    }
}
```

#### Response

```json
{
    "status": 400,
    "result": {
        "rating": [
            "Ensure this value is less than or equal to 5.0."
        ],
        "year": [
            "Ensure this value is less than or equal to 2019."
        ]
    }
}
```

---
### Delete Movie

| Method | Endpoint  | Access |
|--|--|--|
| `DELETE` | `/movie` | Admin |


#### Case 1 : Valid input with token

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "id": 39
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Deleted record",
    "record": {
        "title": "test",
        "id": 39
    },
}
```

#### Case 2 : Not Existing Movie

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "id": 39
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Specified record does not exists",
}
```

---
### Update Movie

| Method | Endpoint  | Access |
|--|--|--|
| `PUT` | `/movie` | Admin |


#### Case 1 : Valid input with token

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "id":40,
        "description":"New Description",
        "rating": 3.6
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Updated record",
    "record": {
        "id": 40,
        "description": "New Description",
        "rating": 3.6
    }
}
```

#### Case 2 : Not Existing Movie

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "id":400,
        "description":"New Description",
        "rating": 3.6,
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Specified record does not exists",
}
```

#### Case 3 : Invalid Data

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "id":40,
        "description":"New Description",
        "rating": 13.6,
        "year": 20122
    }
}
```

#### Response

```json
{
    "status": 400,
    "result": "Invalid Data",
    "record": [
        {
            "rating": 13.6,
            "message": "Rating value should be between 0 - 5"
        },
        {
            "year": 20122,
            "message": "Year value should be between 1980 - current year"
        }
    ]
}
```

---
### Fetch Movies

| Method | Endpoint  | Access |
|--|--|--|
| `GET` | `/movie` | Admin/RegisterdUser |


#### Case 1 : Valid input with token

#### Request - Parameters

`token` = `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im`
`title` = `man`


#### Response

```json
{
    "status": 200,
    "result": "Success fetching movie details",
    "record": [
        {
            "title": "Spider-Man",
            "description": "Spider-Man is a super hero movie",
            "rating": 4.1,
            "year": 2012
        },
        {
            "title": "Batman Begins",
            "description": "After witnessing his parents' death, Bruce learns the art of fighting to confront injustice. When he returns to Gotham as Batman, he must stop a secret society that intends to destroy the city.",
            "rating": 4.4,
            "year": 2005
        },
        {
            "title": "Man of Steel",
            "description": "After Superman discovers that he has extraordinary powers, he decides to use them for doing good. He even fights against members of his own race to defend the people of Earth.",
            "rating": 4.2,
            "year": 2013
        },
        {
            "title": "Batman v Superman: Dawn of Justice",
            "description": "Bruce Wayne, a billionaire, believes that Superman is a threat to humanity after his battle in Metropolis. Thus, he decides to adopt his mantle of Batman and defeat him once and for all.",
            "rating": 4.6,
            "year": 2016
        }
    ]
}
```

#### Case 2 : Empty Result set

#### Request

`token` = `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im`
`title` = `xyz`

#### Response

```json
{
    "status": 200,
    "result": "Empty result-set"
}
```

#### Case 3 : Invalid Data

#### Request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im",
    "data": {
        "id":40,
        "description":"New Description",
        "rating": 13.6,
        "year": 20122
    }
}
```

#### Response

```json
{
    "status": 400,
    "result": "Invalid Data",
    "record": [
        {
            "rating": 13.6,
            "message": "Rating value should be between 0 - 5"
        },
        {
            "year": 20122,
            "message": "Year value should be between 1980 - current year"
        }
    ]
}
```

## User Management Module

### Add User

| Method | Endpoint  | Access |
|--|--|--|
| `POST` | `/user` | Admin |


#### Case 1 : Valid input

#### Request

```json
{
    "email":"admin@gmail.com",
    "password":"admin",
    "data": {
        "email":"jhon@gmail.com",
        "password":"jhon",
        "is_admin":false
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Added new record",
    "record": {
        "email": "jhon@gmail.com",
        "is_admin": false
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
}
```

#### Case 2 : User already exists

#### Request

```json
{
    "email":"admin@gmail.com",
    "password":"admin",
    "data": {
        "email":"jhon@gmail.com",
        "password":"jhon",
        "is_admin":false
    }
}
```

#### Response

```json
{
    "status": 400,
    "result": {
        "email": [
            "users with this email already exists."
        ]
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
}
```

### Delete User

| Method | Endpoint  | Access |
|--|--|--|
| `DELETE` | `/user` | Admin |


#### Case 1 : Valid input

#### Request

```json
{
    "email":"admin@gmail.com",
    "password":"admin",
    "data": {
        "email":"jhon12@gmail.com"
    }
}
```

#### Response

```json
{
    "status": 200,
    "result": "Deleted record",
    "record": {
        "email": "jhon12@gmail.com"
    },
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
}
```

#### Case 2 : User does not exists

#### Request

```json
{
    "email":"admin@gmail.com",
    "password":"admin",
    "data": {
        "email":"xyz@gmail.com",
    }
}
```

#### Response

```json
{
    "status": 400,
    "result": "Specified record does not exists",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
}
```