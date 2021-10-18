from django.urls import path
from .views import login_required, blank

urlpatterns = [
    path('login_required/', login_required),
    path('blank/', blank),
]
