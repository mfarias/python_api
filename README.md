# List users API


## Instructions

  Clone code and run `docker-compose up -d --build`. App should be available in port 5000 and database should be created with 1 million records.
  
  


## Endpoints

  #### 1 - Health check:

* **URL:** /

* **Method:** `GET`
  
* **URL Params:** None

* **Data Params:** None

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** `Users API`
  
----

#### 2 - Get user by id:

* **URL:** /users/:id

* **Method:** `GET`
  
* **URL Params:** `id=[integer]` *(required)*

* **Data Params:** None

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** `{ id : 1, name : "User 1", login: "user1", email: "user1@example.com"  }`
    
----
  
  
 #### 3 - List users:

* **URL:** /users

* **Method:** `GET`
  
* **URL Params:** None

* **Data Params**: 
  * page: `[integer]` number of the page
  * per_page: `[integer]` number of items per page
  * name: `[string]` filter by name
  * login: `[string]` filter by login
  * email: `[string]` filter by email

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:** `[
                    { id : 1, name : "User 1", login: "user1", email: "user1@example.com"  }, 
                    { id : 2, name : "User 2", login: "user2", email: "user2@example.com"  }
                  ]`

