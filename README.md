# Movie API


| Module | Method | Desciption | Endpoint | Details | Access |
|--|--|--|--|--|--|
| User Management | POST | Adds new user | /user | Details | Admin |
| User Management | DELETE | Deletes specified user | /user | Details | Admin |
| Movie | POST | Adds new movie | /movie | Details | Admin |
| Movie | DELETE | Deletes specified movie | /movie | Details | Admin |
| Movie | PUT | Updates specified movie | /movie | Details | Admin |
| Movie | GET | Fetches movie details matching specified keyword | /movie | Details | Admin/Registered User |

## Movie Module

### Add User

| Method | Endpoint  | Access |
|--|--|--|
| POST | /user | Admin |


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
    }
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
    "password":"jhon"
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