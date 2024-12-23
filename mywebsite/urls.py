from django.urls import path
from .views import *

app_name='mywebsite'
urlpatterns=[
    path('',home,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('requested/',requested,name='requested'),
    path('signin/',signin,name='signin'),
]