
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def thread_check(sender, instance, **kwargs):
    print("Signal Thread:", threading.current_thread().name)

# Run in Django shell:
from django.contrib.auth.models import User
import threading

print("Main Thread:", threading.current_thread().name)
User.objects.create(username='thread_test')
