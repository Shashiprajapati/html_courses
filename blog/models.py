from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#  next to wok on SQL
#  we will have to run the command
#  python manage.py makemigrations
#  python manage.py migrate
#  python manage.py createsuperuser
#  then we will give username, email and password to create our blog


# Create your models here.
class Post(models.Model):
    # name = models.CharField(max_length=100)
    place = models.TextField()
    # id = models.TextField()
    qualification = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    name = models.ForeignKey(User, on_delete=models.CASCADE)


# after completing the above task, we would need to run this command to create a file named 0001_initial.py
# python manage.py makemigrations
#  then further we will move on to SQL jobs

# if we want to check the sql code which it automatically writes
# python manage.py sqlmigrate blog 0001

#  it gives the output as
# CREATE TABLE "blog_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "place" text NOT NULL, "qualification" text NOT NULL, "date_posted" datetime NOT NULL, "name_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
# CREATE INDEX "blog_post_name_id_e871f0ab" ON "blog_post" ("name_id");
# COMMIT;

# if we make any change in the database we will need to write this command
# python manage.py migrate

#  now we will create shell in cmd
# python manage.py shell
#  from blog.models import Post
# from django.contrib.auth.models import User
#  User.objects.all()
