from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# user table--------------------------------------------------------------------
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

     

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    
    phone=models.CharField(verbose_name="phone", max_length=15)
    
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username

    


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

# end user table ----------------------------------------------------------------------------------------



# Create your models here.
class About(models.Model):
    # id: int id  is automatically made
    projectname = models.CharField(max_length=100)
    projecttype = models.CharField(max_length=500)
    image =models.ImageField(upload_to="home/")

class Message(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    message = models.CharField(max_length=30000, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Projectorder(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    project_type = models.CharField(max_length=200, null=True)
    project_name = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=200, null=True)
    project_description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
class Service(models.Model):
    # id: int id  is automatically made
    Project_name = models.CharField(max_length=100)
    Project_description = models.CharField(max_length=500)
    Project_explanations = models.CharField(max_length=30000)
    image =models.ImageField(upload_to="home/")