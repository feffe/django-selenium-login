from django.urls import path, include

urlpatterns = [
    path('test/', include('test_.urls')),
]
