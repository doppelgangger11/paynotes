from django.urls import path
from .views import *

app_name = 'paymanager'

urlpatterns = [ 
    path('landing/', landing_page_view, name='landing/paymanager') 
]