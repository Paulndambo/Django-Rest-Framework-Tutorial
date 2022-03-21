from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email_confirmed = models.BooleanField(default=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initial_email = self.email

    def save(self, *args, **kwargs):
        if self.email != self._initial_email:
            self.email_confirmed = False
        super().save(*args, **kwargs)