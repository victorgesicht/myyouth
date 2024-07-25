from django.db import models

# Create your models here.




    
class general_info(models.Model):
    email=models.EmailField(max_length=50, default='twobigfeetninja@gmail.com')
    phone=models.CharField(default='0712-345-678', max_length=50)
    web_app_name=models.TextField(default='glowing up')
    location=models.TextField(default='Kenya')
    open_hours=models.CharField(default='9-5, every weekday', max_length=50 )
