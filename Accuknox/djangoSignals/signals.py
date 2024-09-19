from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Accuknox, AccuknoxMessage
import time
import threading


@receiver(post_save, sender=Accuknox)
def handler(sender, instance, **kwargs):
    print(f"Signal thread id : {threading.get_ident()}")
    print("Signal initiated")
    # time.sleep(5)
    print("Signal Received task finished")


@receiver(post_save, sender=Accuknox)
def handler(sender, instance, **kwargs):
    AccuknoxMessage.objects.create(message=f"signal created via {instance}")