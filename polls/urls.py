from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),
]
