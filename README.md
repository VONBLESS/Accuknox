# Accuknox
answers to https://docs.google.com/forms/d/e/1FAIpQLSeIZq-YPIre8aMVwxE5BwsR-tC0S_bu68gDMePmWXVP50hKxA/viewform





Answers are in Accunox -> djangoSignals app please refer those as refrence  
Questions for Django Trainee at Accuknox

Topic: Django Signals

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer  
Django, signals are executed synchronously
So have worked with post_save signal so here’s an example

```
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class Accuknox(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a delay
    print("Signal handler finished")
 ```

So as i have added in my github page
I added my model (Accuknox) in the admin page where one can create an entry so while saving the model one must wait for another 5 seconds to add another entry.
This proves that signals are send and handler are executed immediately and one cannot add another within the next second as it is in the same thread 

Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer  
To answer this we can check if thread id of the signal handler and the caller match, which they do 
Similarly in Accuknox model we can add
```
Import thrading 

‘’’ same as above ‘’’
@receiver(post_save, sender=Accuknox)
def handler(sender, instance, **kwargs):
    print(f"Signal thread id : {threading.get_ident()}")
    time.sleep(5)
```
In admin.py

```
from django.contrib import admin
from .models import Accuknox
import threading

class AccuknoxAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print(f"Caller thread if : {threading.get_ident()}")
        super().save_model(request, obj, form, change)
        print("Saved via admin")


admin.site.register(Accuknox, AccuknoxAdmin)
```
Its in github repo one can demonstrate via creating a superadmin and then logging into admin site
So in my case the thread ids match

    

Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer  
Yes, they run in the same database transaction as the caller. i.e a signal from a model creation trigger another model instance creation and the creation fails for the second model none of the model instance is created 
These are my models
```
class Accuknox(models.Model):
    name = models.CharField(max_length=120)


class AccuknoxMessage(models.Model):
    message = models.TextField()
```
These are my signals
```
@receiver(post_save, sender=Accuknox)
def handler(sender, instance, **kwargs):
    print("Signal initiated")
    print("Signal Received task finished")


@receiver(post_save, sender=Accuknox)
def handler(sender, instance, **kwargs):
    AccuknoxMessage.objects.create(message=f"signal created via {instance}")
```
You can create a view or add it to admin model i created a view where
```
def tes_transaction_view(request):
    try:
        with transaction.atomic():
            instance = Accuknox(name="Hello World")
            instance.save()
            print(f"Signal Count {AccuknoxMessage.objects.count()}")

            raise Exception("Rollback occured")

    except Exception as e:
        print(f"Exception {e}")

    print(f"Signal Count {AccuknoxMessage.objects.count()}")
    return HttpResponse("hello")
```
So initially the signal count will be 2 and then 1
You can access this route below to assert my statement after running the project locally,  
http://127.0.0.1:8000/test-signal/
and check the terminal or logs for reference
I.e Accuknox model triggers signal to create a AccuknoxMessage object and it is not creat.  
Then exception is raised and rollback happens so in the admin panel you can see no instance of Accuknox model is created






Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

Answer  
```
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
        
rect = Rectangle(100, 100)
for dim in rect:
    print(dim, end= " ")    
```

you can access to answers in   
http://127.0.0.1:8000/test-rectangle/

