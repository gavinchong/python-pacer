## Task 1

### Endpoints
<code>GET</code> http://127.0.0.1:8000/api/get_score

The following is a Task 1 Simple JSON result:

**Header**

	Accept: application/json
	Content-Type: application/json
	Authorization: Token {token}

**Success**
```JSON
{
    "status": "success",
    "result": {
        "id": 2,
        "point": 100,
        "created_at": "2022-09-21T00:00:00Z",
        "user": 1
    }
}
```

**Failed**
```JSON
{
    "status": "success",
    "result": {},
    "message": "No record found"
}
```

### Testcase

Running testcase command
--------------------------

```
$ python manage.py test
```

## Task 2
http://127.0.0.1:8000/admin

## Task 3

Running command below to create migration file
--------------------------

```
$ python manage.py makemigrations
Migrations for 'api':
  api/migrations/0001_initial.py
    - Create model Score
```

Running command below to run migration files
--------------------------

```
$ python manage.py migrate
```