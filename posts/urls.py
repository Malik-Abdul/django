from django.urls import path, include # 1. Import the include() function: from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list),
]