# WorkloadTest-CloudComp

This is part of 2110524 Cloud Computing Technologies 2020/2

## Install Database:

    $ sudo yum install mariadb-server
    $ sudo systemctl enable mariadb
    $ sudo systemctl start mariadb
    $ sudo systemctl is-enabled mariadb
    $ mysqladmin -u root password 'password'
    $ mysql -uroot -p

    $ CREATE DATABASE ebdb;
    $ GRANT ALL PRIVILEGES ON *.*sel TO 'root'@'%' IDENTIFIED BY '';

    $ use ebdb;
    $ SHOW TABLES;
    $ select * from auth_user;

## Install Backend Server:

    $ sudo yum install git python3 mysql-devel

    $ git clone https://github.com/armykongtap/WorkloadTest-CloudComp.git

updte database address.

    $ cd WorkloadTest-CloudComp
    $ cd backend
    $ sudo nano setting.py

under DATABASES variable update database address. Then run server.

    $ sudo python3 -m pip install -U pip
    $ sudo python3 -m pip install -r requirements.txt

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    $ python3 manage.py runserver 0.0.0.0:8000

To access admin page:

    $ python3 manage.py createsuperuser --username=admin --email=admin@mail.com

and go to http://127.0.0.1:8000/admin/

### Create user

    curl -X POST http://127.0.0.1:8000/auth/users/ --data-raw {'username':'user1','password':'aNzFdqBu'}

### Login

    curl -X POST http://127.0.0.1:8000/auth/token/login/ --data-raw {'username':'user1','password':'aNzFdqBu'}

### Update 'password'

    curl -LX POST http://127.0.0.1:8000/auth/users/set_password/ --data-raw {'new_password':'aNzFdqBu','username':'user1','password':'aNzFdqBu'}

more detail: https://djoser.readthedocs.io/en/latest/index.html
