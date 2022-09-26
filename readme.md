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

![alt text](https://github.com/gavinchong/python-pacer/blob/main/Screenshot%202022-09-26%20at%202.49.42%20PM.png)

## Task 3


```python
class Score(models.Model):
    class Meta:
        db_table = 'score'
    
    point = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    created_by = models.IntegerField(null=True) <-- add new field
```


Running command below to create migration file
--------------------------

```
$ python manage.py makemigrations
```

Running command below to run migration files
--------------------------

```
$ python manage.py migrate
```

## Additional Task

### Auth Token

Running command below to create token
--------------------------

```
$ python manage.py drf_create_token [username]
```
