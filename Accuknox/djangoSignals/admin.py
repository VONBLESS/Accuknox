from django.contrib import admin
from .models import Accuknox
import threading

# Register your models here.
class AccuknoxAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print(f"Caller thread if : {threading.get_ident()}")
        super().save_model(request, obj, form, change)
        print("Saved via admin")


admin.site.register(Accuknox, AccuknoxAdmin)
