import null as null
from django.contrib.auth.models import User
from django.db import models
from utils.roles import *


class UserProfile(models.Model):
    bio = models.TextField(max_length=100, null=True, blank=True),
    roles = models.SmallIntegerField(choices=USER_ROLE, default=USER_ROLE_GUEST),
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
