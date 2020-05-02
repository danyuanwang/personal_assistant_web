from django.urls import path
from . import views

app_name = 'personal_assistant_app'
urlpatterns = [
# Home Page
    path('', views.index, name='index'),
]
