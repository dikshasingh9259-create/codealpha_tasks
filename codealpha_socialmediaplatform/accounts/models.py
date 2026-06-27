from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=500)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"