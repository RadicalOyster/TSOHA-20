**Installation Guide**

**Requirements**

* Python 3.7 (may run on newer or older versions, but has not been tested)
 * pip
 * venv

**Installing and running the database locally**

* Download the project from the [repository](https://github.com/RadicalOyster/TSOHA-20-Dungeons-and-Dragons-Database) and unpack it or use git clone to copy the repository onto your computer

* In the main project directory launch the python virtual environment:

>python3 -m venv venv
>
>source venv/bin/activate

* Install dependencies:


>pip install -r requirements.txt


* Launch the application:

>python run.py

An admin user with the credentials Username: "Admin", Password: "Admin" is automatically created when the application is launched.

**Installing the database on Heroku**

* Requirements for this step:
  * git
  * Heroku CLI


> heroku create [application_name]
>
> git remote add heroku [repository address]
>
> git add .
>
> git commit -m "hello world"
>
> git push heroku master


