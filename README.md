## E_Commerce Api

**Methods**

GET: Used to retrieve data from a server.

POST: Used to send data to the server to create a new resource.

PUT: Used to update or replace an existing resource.

DELETE: Used to remove a resource from the server.

**poetry commands**

add drivers
```shell
mac
poetry add fastapi uvicorn\[standard\] sqlmodel psycopg 

window
poetry add fastapi uvicorn[standard] sqlmodel psycopg 
```

**=================================================================**

```shell
user = User(**user.model_dump())
```
**Note** # 1- The model_dump() method likely converts the 'user' instance to a dictionary. 2- Then, the dictionary is unpacked using ** and passed as keyword arguments 3- to create a new User instance.


SQL_Alchemy_model(**form_data.model_dump())
#### Full Flow :- user = User(**form_data.model_dump())
**1- Pydantic Model:** User instance (form_data) holds user details.

**2- Convert to Dictionary:** form_data.model_dump() converts the instance to a dictionary.

**3- Dictionary Unpacking:** **form_data.model_dump() unpacks the dictionary into keyword arguments.

**4- Create User Object:** User(**form_data.model_dump()) creates a new User object with the provided details.

**model_dump()** method in Pydantic :- converts a model instance into a dictionary with the model's attribute names as keys and their corresponding values.

[returns a standard Python dictionary (dict) containing the attributes and values of the model instance.](https://stackoverflow.com/questions/77476105/can-pydantic-model-dump-return-exact-type)

**Tutorials**

[fastapi- stept1](https://fastapi.tiangolo.com/tutorial/first-steps/)

[SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)

[Models with Relationships in FastAP](https://sqlmodel.tiangolo.com/tutorial/fastapi/relationships/#why-arent-we-getting-more-data)

[FastAPI Path Operations for Teams - Other Models](https://sqlmodel.tiangolo.com/tutorial/fastapi/teams/#path-operations-for-teams)

[SQLModel Update Data with FastAPI](https://sqlmodel.tiangolo.com/tutorial/fastapi/update/#create-the-update-path-operation)



# e_commerce-api
