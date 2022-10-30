from django.urls import path
from pharmacy.views import create_pharmacy
app_name = 'pharmacy'

urlpatterns = [
    path('create_pharmacy', create_pharmacy, name='create_pharmacy'),

]