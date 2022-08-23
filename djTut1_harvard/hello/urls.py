from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="hello.index"),
    path("<str:name>", views.greeting, name="hello.greeting"),
    path("devid/", views.devid, name="hello.devid"),
    path("morgan/", views.morgran, name="hello.morgan"),
]
