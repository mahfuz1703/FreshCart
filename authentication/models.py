from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="user_photos", blank=True, default="user_photo/default-user.jpg")
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username