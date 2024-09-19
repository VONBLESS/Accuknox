from django.urls import path
from . import views

urlpatterns = [
    path('test-signal/', views.tes_transaction_view, name='test-signal'),
    path('test-rectangle/', views.test_rectangle_view, name='test-rectangle'),
]