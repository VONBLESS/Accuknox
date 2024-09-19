from django.db import transaction
from django.http import HttpResponse
from .models import AccuknoxMessage, Accuknox


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


# Create your views here.
def tes_transaction_view(request):
    try:
        with transaction.atomic():
            instance = Accuknox(name="Hello World 1")
            instance.save()
            print(f"Signal Count {AccuknoxMessage.objects.count()}")

            raise Exception("Rollback occured")

    except Exception as e:
        print(f"Exception {e}")

    print(f"Signal Count {AccuknoxMessage.objects.count()}")
    return HttpResponse("hello")


def test_rectangle_view(request):
    rect = Rectangle(100, 100)
    ans = []
    for dimension in rect:
        print(dimension)
        ans.append(dimension)

    return HttpResponse(f"{ans}")



