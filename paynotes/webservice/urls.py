from django.urls import path
from .views import *

app_name = 'webservice'

urlpatterns = [ 
    path('landing/', landing_page_view, name='landing_webservice') 
]