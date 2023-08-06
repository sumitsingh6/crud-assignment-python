# Python Assignment: CRUD Api
**A Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API**

## Using docker to run 
Make sure you have docker installed in your machine.
To check if docker is installed run
`docker --version`

then to execute this app run:
 `docker run -p 8000:8000 sumitkrsingh98/crud-python-app`
## The REST API
Host: http://127.0.0.1:8000

### 1. To fetch all the users from the database
`GET /users`


**Response**:

    [{"_id":{"$oid":"id123"},"name":"user1","email":"user1@user1.com","password":"pass1"},{"_id":{"$oid":"id124"},"name":"user2","email":"user2@user2.com","password":"pass2"}]
![enter image description here](https://user-images.githubusercontent.com/38861211/258647832-d1414852-08b8-4ad7-8dea-acf6cfd8bb5c.png)
### 2. To return the user with the specified ID

`GET /users/<id>`


**Response**
`[{"_id":"$oid":"id123"},"name":"user1","email":"user1@user1.com","password":"pass1"}]`

![enter image description here](https://user-images.githubusercontent.com/38861211/258647712-4a046cc3-46be-4df6-a18c-406371a3568a.png)

### 3. To create a new user with the specified data

`POST /users`


**Response**
`{"acknowledged":true,"inserted_id":"userid"}`

![enter image description here](https://user-images.githubusercontent.com/38861211/258662655-d38fe5c1-88db-4a65-a133-9eb333256b0b.png)

### 4. To update a user with the specified ID with the new data.

`PUT /users/<id>`


**Body**
`{"name":"Test1","email":"test@testupdate.com","password":"password update"}`

(only add fields that needs to be updated )


**Response**
`{"acknowledged":true,"matched_count":1,"modified_count":1,"upserted_id":null}`

![enter image description here](https://user-images.githubusercontent.com/38861211/258662723-3d3e5880-5d5a-4556-a451-12a179e6a275.png)

### 5. Deletes the user with the specified ID
`DELETE /users/<id>`


**Response:**
`{"acknowledged":true,"deleted_count":1}`

![enter image description here](https://user-images.githubusercontent.com/38861211/258662780-a2c6eed9-db9b-4cd7-a8dc-bd42f4fc2b7c.png)
