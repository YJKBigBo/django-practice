from xml.etree.ElementInclude import include
from django.urls import path

from todo.views import todos

urlpatterns = [
	path('', todos),
    
]