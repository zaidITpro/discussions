from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'user_userprofile'

@receiver(post_save, sender=CustomUser)
def create_user_customuser(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_customuser(sender, instance, **kwargs):
    instance.UserProfile.save()
