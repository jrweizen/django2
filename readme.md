###DEF.: Repo to learn django with Postgres and deploy into Heroku
<br>https://django2-jocelino.herokuapp.com/

###Install Pre-requisites
<br>⇒  pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage
<br>⇒  pip freeze > requirements.txt

<br>git init ... config git here

### Django environment, and freeze into requirements file(similar to package-json)
<br> ⇒  django-admin startproject django2 .
<br> ⇒  django-admin startapp core

#### Install Mysql(after moved to postgres, due to heroku free plan requirements):
<br>⇒  brew install mysql-connector-c          
<br>⇒  pip install MySQL          

<br>⇒  python manage.py migrate
<br>⇒  python manage.py createsuperuser

####Settings file
<br>altered configs - see the file itself. the order matters inside brackets


#### HEROKU
<br>⇒  heroku login
<br>⇒  git add .
<br>⇒  git commit -m 'message'
<br>⇒  git push heroku master
<br>⇒  heroku run python manage.py migrate

<br>




