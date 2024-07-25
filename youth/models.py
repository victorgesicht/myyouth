from django.db import models

# Create your models here.

class book(models.Model):
    title=models.TextField()
    author=models.TextField()


class podcast(models.Model):
    title=models.CharField(max_length=50, default='Conspiracy Theories')
    genre=models.TextField()


class spotify_records(models.Model):
    year=models.DateTimeField(auto_created=True)
    image=models.ImageField()
    
class chess_awards(models.Model):
    tournament_name=models.TextField()
    image=models.ImageField()

class work_experience(models.Model):
    job_title=models.TextField()
    organization=models.TextField()
    year=models.DateField(auto_created=True)
    
class general_info(models.Model):
    email=models.EmailField(max_length=50, default='twobigfeetninja@gmail.com')
    phone=models.CharField(default='0712-345-678', max_length=50)
    web_app_name=models.TextField(default='glowing up')
    location=models.TextField(default='Kenya')
    open_hours=models.CharField(default='9-5, every weekday', max_length=50 )