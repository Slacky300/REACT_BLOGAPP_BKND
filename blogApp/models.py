from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from autoslug import AutoSlugField

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError('User must provide a email')
        
        user = self.model(
            email = email,
            name = name
        )


        user.set_password(password)
        user.save(using = self._db)

        return user


    def create_superuser(self, email, name, password = None):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length = 50,unique=True)
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='userProfile',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(models.Model):

    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True,blank=True, db_constraint=False)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='post/',null=True,blank=True)
    desc = models.TextField()
    uploadedOn = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = "title",unique = True)
    likes = models.ManyToManyField(UserAccount,blank=True)
    file = models.FileField(upload_to='files/',null=True,blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    post = models.ForeignKey(Post,models.DO_NOTHING, db_constraint=False)
    byUser = models.ForeignKey(UserAccount,on_delete=models.DO_NOTHING, db_constraint=False)
    text = models.CharField(max_length=250)
    cmntDate = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(UserAccount, related_name = "userCmnt", blank=True)

    def __str__(self):
        return str(self.byUser)