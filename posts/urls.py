from django.urls import path, include # 1. Import the include() function: from django.urls import include, path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.post_list, name="list"),
    path('<slug:slug>', views.post_page, name="page"),
]