from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path("", views.ProductView.as_view(), name="index"),
    path("create/", views.create, name="create"),
]
