# WorkloadTest-CloudComp
This is part of 2110524 Cloud Computing Technologies 2020/2

To run this project:

.. code-block:: bash
	$ pip install -r  requirements.txt
	$ python manage.py makemigrations
	$ python manage.py migrate
	$ python manage.py runserver

Endpoints
============================

Create user
http://127.0.0.1:8000/auth/users/
{
    "username": "user3",
    "password": "7zNm3K&PA!NE"
}

Login
http://127.0.0.1:8000/auth/token/login/
{
    "username": "user3",
    "password": "7zNm3K&PA!NE"
}

Update password
http://127.0.0.1:8000/auth/users/set_password/
{
    "new_password": "7zNm3K&PA!NE",
    "re_new_password": "7zNm3K&PA!NE",
    "current_password": "7zNm3K&PA!NE"
}

To access admin page:

.. code-block:: bash
	$ python manage.py createsuperuser --username=admin --email=admin@mail.com

and go to http://127.0.0.1:8000/admin/

more detail: https://djoser.readthedocs.io/en/latest/index.html