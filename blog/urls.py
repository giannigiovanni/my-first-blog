from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('giannigiov.pythonanywhere.com', views.post_list, name='post_list')
]