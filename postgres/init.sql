CREATE TABLE IF NOT EXISTS user_model (
   id INT PRIMARY KEY,
   name varchar(150) NOT NULL,
   login varchar(50) NOT NULL,
   email varchar(100) NOT NULL
);

COPY user_model (id,name,login,email)
FROM '/var/lib/postgresql/csv/users.csv'
DELIMITER ',' CSV HEADER;