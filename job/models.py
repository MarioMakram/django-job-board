from django.db import models

# Create your models here.

'''
Djingo model fields:
    - html widget
    - validation
    - db size

after any edit you have to user two commands
    #python manage.py makemigrations
    #python manage.py migrate
and then add this edit class to admin to appear in admin panal
    from .models import Job
    admin.site.register(Job)
'''
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Tome','Part Tome'),

)

class Job(models.Model):
    title = models.CharField(max_length=100)  #column
    # location = 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField (default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=15)



    def __str__(self):
        return self.name
    