1. to setup ven : python3 -m venv <virtual_environment_name>
2. to activate ven: source bin/activate
3. to install Django: pip install django  
   4 to create Django project: django-admin startproject <project_name>
4. cd <project_name>
5. to create app inside the project: python manage.py startapp <app_name>
6. to create requirement : pip freeze > requirements.txt
7. to install requirements : pip install -r requirements.txt
8. to run the server : python manage.py runserver

---------- General_info_about_django -----------

1. to registered app: go to settings.py then add it to the list INSTALLED_APP
2. to ignore files: nano.gitignore
3. to make migrations: python manage.py makemigrations
4. to apply those new changes: python manage.py migrate
5. to create super user: python manage.py createsuperuser
6. to test :python manage.py tes
7. to run the server : python manage.py runserver
8. To know the path: pwd
9. to Register your model Readmin.site.register(<ModelName>)

--------- First_Step ----------

1. go to settings.py file to register <app_name> under INSTALLED_APPS
2. go to your app and create your models
3. makemigrations and migrate because you created a model
4. Register your model in admin.py
   a. import your model
   b. admin.site.register(<ModelName>)
5. create super user to access the admin page
6.
