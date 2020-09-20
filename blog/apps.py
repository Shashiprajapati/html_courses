from django.apps import AppConfig

# to create blog, we have the command
# python manage.py startapp blog
# it create a blog folder in the project folder, then we can work on views, apps, models.
#  blogurl we nedd to create by ourselves to connect it with url of the main project
# further we can create folder for html and css like templates and static we have done for this project


#  next to wok on SQL
#  we will have to run the command
#  python manage.py makemigrations
#  python manage.py migrate
#  python manage.py createsuperuser
#  then we will give username, email and password to create our blog


class BlogConfig(AppConfig):
    name = 'blog'
