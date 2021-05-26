# List users API


## Getting started

 ```sh
 git clone https://github.com/mfarias/python_api.git
 ```
 ```sh
 docker-compose up --build
 ```  
  Access `localhost:5000`
  
  


## Endpoints

  #### 1 - Health check:

* **URL:** /healthcheck

* **Method:** `GET`

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** `Users API is running.`
  
----

#### 2 - Get user by id:

* **URL:** /users/:id

* **Method:** `GET`
  
* **URL Params:** `id=[integer]` *required*

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:**  
  ```json
  {
    "id": 1,
    "name": "user 1",
    "login": "user1",
    "email": "user1@example.com"
  }
  ```
    
----
  
  
 #### 3 - List users:

* **URL:** / or /users

* **Method:** `GET`

* **Query Params**: 
  * `page=[integer]`: *page number. If not informed, the default value is 1.*
  * `per_page=[integer]`: *number of items per page. If not informed, the default value is 5.*
  * `name=[string]`: *filter by name* 
  * `login=[string]`: *filter by login*
  * `email=[string]`: *filter by email*

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** 
  ```json
  [
    {
        "id": 1,
        "name": "User 1",
        "login": "user1",
        "email": "user1@example.com"
    },
    {
        "id": 2,
        "name": "User 2",
        "login": "user2",
        "email": "user2@example.com"
    }
  ]
  ```

