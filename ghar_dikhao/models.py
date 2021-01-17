from django.db import models
from django.contrib.auth.forms import User
from django.utils import timezone
# Create your models here.
house = (
    ('house','HOUSE'),
    ('banglow', 'BANGLOW'),
    ('apartment','APARTMENT'),
    
)
select_bool=(
    ('yes',"YES"),
    ('no',"NO")
)

class advertisment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=5,blank=True,null=True)
    title=models.CharField(max_length=70 )
    state=models.CharField(max_length=70)
    district=models.CharField(max_length=70 )
    bedroom=models.IntegerField(error_messages={'invalid':'Enter a valid bedroom'})
    balcony=models.CharField(max_length=10,choices=select_bool,default="no")
    bathroom=models.IntegerField()
    cost=models.IntegerField()
    description=models.CharField(max_length=700)
    img=models.ImageField(upload_to="myimage")
    category=models.CharField(max_length=10,choices=house,default="house")
    date = models.DateTimeField(default=timezone.now)
    view_count=models.IntegerField(default=0)
    
class contactmodel(models.Model):
    email=models.EmailField(max_length=250)
    phone=models.TextField(max_length=10)
    subject=models.TextField(max_length=500)
    message=models.TextField(max_length=500)

class extenduser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.TextField(max_length=100, default="")
    last_name=models.TextField(max_length=100, default="")
    email=models.TextField(max_length=100, default="")
    phone=models.TextField(max_length=100, default="")
    city=models.TextField(max_length=100, default="")
    state=models.TextField(max_length=100, default="")
    
