from django.db import models
<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, nom, point, password=None):
        """
        Creates and saves a User
        """
        if not nom:
            raise ValueError('Users must have an nom address')

        user = self.model(
            nom=nom,
            point=point,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nom, point, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            nom=nom,
            password=password,
            point=point,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    nom = models.CharField(
        verbose_name='speudo',
        default='SOME STRING',
        max_length=20,
        unique=True
        )
    point =models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'nom'
    REQUIRED_FIELDS = ['point']

    def __str__(self):
        return self.nom

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
=======
=======
>>>>>>> refs/remotes/origin/master
from django.contrib.auth.models import User
from django.urls import reverse

class point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point= models.IntegerField()

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('point-detail', kwargs={'pk': self.pk})
<<<<<<< HEAD
>>>>>>> 37490fcfc9b9789a29ca4709225c286298a7f7bb
=======
>>>>>>> refs/remotes/origin/master

class flag(models.Model):
    num_faille  = models.IntegerField()
    flag        = models.CharField(max_length=50)

<<<<<<< HEAD
<<<<<<< HEAD
    def create_flag(self, num_faille, flag):
        """
        Creates and saves a flag
        """
        if not flag:
            raise ValueError('flag must have an flag')
        if not num_faille:
            raise ValueError('flag must have an num_faille')
        flag = self.model(
            num_faille=num_faille,
            flag=flag,
        )
        flag.save(using=self._db)
        return flag


    def __str__(self):
        return  str(self.num_faille)
=======
    def __str__(self):
        return self.num_faille
>>>>>>> 37490fcfc9b9789a29ca4709225c286298a7f7bb
=======
    def __str__(self):
        return self.num_faille
>>>>>>> refs/remotes/origin/master

    def get_absolute_url(self):
        return reverse('flag-detail', kwargs={'pk': self.pk})
