from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    point= models.IntegerField()

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('point-detail', kwargs={'pk': self.pk})

class flag(models.Model):
    num_faille  = models.IntegerField()
    flag        = models.CharField(max_length=50)

    def __str__(self):
        return self.num_faille

    def get_absolute_url(self):
        return reverse('flag-detail', kwargs={'pk': self.pk})
