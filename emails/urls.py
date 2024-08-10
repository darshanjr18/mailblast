from django.urls import path
from .views import submit_details, success, send_bulk_emails

urlpatterns = [
    path('submit/', submit_details, name='submit_details'),
    path('success/', success, name='success'),
    path('send_bulk_emails/', send_bulk_emails, name='send_bulk_emails'),
   
]
