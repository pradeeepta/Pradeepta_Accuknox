
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def slow_receiver(sender, instance, **kwargs):
    print("Signal started...")
    time.sleep(5)
    print("Signal finished...")

# Run this test in Django shell:
from django.contrib.auth.models import User
import time

start = time.time()
User.objects.create(username='test_user')
end = time.time()
print("Total time:", end - start)
