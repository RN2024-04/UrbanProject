from django.db import models


class PeopleReg(models.Model):
    username=models.CharField(max_length=150, default='')
    password=models.CharField(max_length=150, default='')
    password2=models.CharField(max_length=150, default='')
    USERNAME_FIELD = 'username'
    def save(self, *args, **kwargs):
        # this will take care of the saving
        super(PeopleReg, self).save(*args, **kwargs)
