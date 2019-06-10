from django.urls import path
from .views import BebidasView, SingleBebidasView


app_name = "bebidas"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('bebidas/', BebidasView.as_view()),
    path('bebidas/<int:pk>', SingleBebidasView.as_view())
]
