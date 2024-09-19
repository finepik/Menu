from django.urls import path

from .views import MenuView

app_name = 'menuapp'

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
]
