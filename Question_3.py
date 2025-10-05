
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction, models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default='')

@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    print("Signal creating Profile...")
    Profile.objects.create(user=instance, bio="Created in signal")

# Run this in Django shell:
from django.contrib.auth.models import User
from django.db import transaction
from app.models import Profile

try:
    with transaction.atomic():
        user = User.objects.create(username='rollback_test')
        raise Exception("Rollback!")
except:
    pass

print("Profiles count:", Profile.objects.count())
