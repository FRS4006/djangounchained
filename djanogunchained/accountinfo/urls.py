from django.urls import path
from . import views

urlpatterns = [        
    path('signupaccount/', views.signupaccount, name='signupaccount'),
]