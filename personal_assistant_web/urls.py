"""personal_assistant_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from personal_assistant_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'ConversationLogViewSet', views.ConversationLogViewSet)

urlpatterns = [
    path('admin/', (admin.site.urls)),
    path('api/', include(router.urls)),
    path('', include("personal_assistant_app.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/from-user/', views.from_user, name="from_user"),
    path('api/take_action/', views.take_action, name="take_action"),
    path('api/generate_nl/', views.generate_nl, name="generate_nl"),
 ]
