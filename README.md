# *DJANGO REST API SOCIAL NETWORK* (test project)
<br />

## Installation
### (PostgreSQL is used in the project. You need to install it first)
<br/>

Make directory for the project:
```
$ mkdir <project_dir>
```
Run virtual environment into project directory:
```
$ python3 -m venv <env_dir> and activate it source bin/activate
```
Clone git repository into environment directory :
```
$ git clone https://github.com/SSRomanSS/social_network.git
```
Run installation in messenger directory:
```
$ pip install -r requirements.txt
```
```
$ python manage.py migrate
```
```
$ python manage.py createsuperuser (Remember superuser login and password!)
```
```
$ python manage.py runserver
```
After that you can check the result on: http://localhost:8000

Don't forget to use superuser credentials to view API on browser.

## Links
GET all posts 
```
http://localhost:8000/api/posts/list/
```
GET all likes
```
http://localhost:8000/api/posts/likes/list/
```
GET single post by unique identifier like counting
```
http://localhost:8000/api/posts/<unique_message_identifier>/likes_count/
```
> unique_message_identifier = Primary Key in a database

GET method for like counting by date
```
http://localhost:8000/api/analitics/?date_from=<yyyy-mm-dd>&date_to=<yyyy-mm-dd>
```
GET method for getting list of users who like single message by unique identifier
```
/api/posts/<unique_message_identifier>/users_like/
```
> unique_message_identifier = Primary Key in a database

POST method for creating a new post
```
http://localhost:8000/api/posts/post_message/
```
POST method for like a post
```
http://localhost:8000/api/posts/<unique_message_identifier>/add_like/
```
> unique_message_identifier = Primary Key in a database

POST method for unlike a post
```
http://localhost:8000/api/posts/<unique_message_identifier>/unlike/
```
> unique_message_identifier = Primary Key in a database

GET all users 
```
http://localhost:8000/api/users/list/
```
POST method for create user
```
http://localhost:8000/api/user/create/
```
POST method for create user
```
http://localhost:8000/api/user/login/
```
GET/POST method for check/update user info
```
http://localhost:8000/api/user/login/
```
POST method for getting JWS token
```
http://localhost:8000/api/user/get_token
```



















