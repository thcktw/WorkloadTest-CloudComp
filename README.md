# WorkloadTest-CloudComp

This is part of 2110524 Cloud Computing Technologies 2020/2

To run this project:

    $ pip install -r  requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver

To access admin page:

    $ python manage.py createsuperuser --username=admin --email=admin@mail.com

and go to http://127.0.0.1:8000/admin/

## Create user

    curl -X POST http://127.0.0.1:8000/auth/users/ --data-raw {'username':'user1','password':'aNzFdqBu'}

## Login

    curl -X POST http://127.0.0.1:8000/auth/token/login/ --data-raw {'username':'user1','password':'aNzFdqBu'}

## Update 'password'

    curl -LX POST http://127.0.0.1:8000/auth/users/set_password/ -H 'Authorization: Token b704c9fc3655635646356ac2950269f352ea1139' --data-raw {'new_password':'aNzFdqBu','re_new_password':'aNzFdqBu','current_password':'aNzFdqBu'}

more detail: https://djoser.readthedocs.io/en/latest/index.html
