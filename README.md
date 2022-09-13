Quickstart

Our mission is to create a REST API for the user to write comments about the characters and episodes of the Rick&Morty anime.

-- Requirements --

The technical requirements for this project are as follows:

- Use of Python 3.8.

- Use of a relational SGDB: MySQL

- Use of FastApi


-- To run the project --

- Clone the project: git clone https://github.com/ltifi/Rick-Morty-Project.git

- Create the database:

1- docker-compose exec db sh <br />
2- mysql -uroot -p <br />
3- create database "databse name"; <br />
4- cd Rick-Morty-Project <br />

- make start

-- To run the project Scripts --

1- docker-compose exec app sh <br />
2- python3 script.py <br />
3- python3 script_scrapping.py <br />

-- To test the APIs --

1-Go to 0.0.0.0:80/docs <br />
2-Test apis.
