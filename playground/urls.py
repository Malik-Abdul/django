from django.urls import path
from . import views

# note this is url configuration module, every app have its own url configuration.
urlpatterns=[
    path('hello/', views.say_hello) # views.say_hello we are not calling this fuctions, instead we are passing the reference
]
# Now we will import this url configuration into the main url configuration of this project