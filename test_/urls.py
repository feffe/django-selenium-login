from django.conf.urls import url
from .views import login_required, blank

urlpatterns = [
    url(r'^login_required', login_required),
    url(r'^blank', blank),
]
