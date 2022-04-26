Quickstart

Our mission is to create a REST API that for the user to write comments about the characters and episodes of the Rick&Morty anime.

-- Requirements --

The technical requirements for this project are as follows:

- Use of Python 3.8.

- Use of a relational SGDB: MySQL

- Use of FastApi


-- To run the projet --

- git clone https://github.com/ltifi/Rick-Morty-Project.git

- cd Rick-Morty-Project

- pip3 install -r requirements.txt

-- Then create .env file (or rename and modify .env.example) in project root and set environment variables for application --

- SQLALCHEMY_DB_URL='mysql+pymysql://root@127.0.0.1:3306/anime'
- SECRET_KEY='secret key'
- ALGORITHM='HS256'
- ACCESS_TOKEN_EXPIRE_MINUTES=30

-- To run the web application in debug mode --

uvicorn app.main:app --reload

- Application will be available on localhost in your browser.

- All routes are available on /docs paths with Swagger.
