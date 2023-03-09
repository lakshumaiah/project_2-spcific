from django.urls import path
from csk.views import *
app_name='kamalakuru'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('jadeja/',jadeja,name='jadeja'),
]