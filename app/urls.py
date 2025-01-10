from django.urls import path
from .views import *

urlpatterns = [
    path('spells/', SpellAPIViews.as_view(), name="spell")
    
]