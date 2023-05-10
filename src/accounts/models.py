from django.db import models
from django.contrib.auth.models import User
from .management.commands.startvoting import Voter as mpcVoter

# Create your models here.

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voter = mpcVoter()
