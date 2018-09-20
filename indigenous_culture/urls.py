from django.urls import  path
from .views import *
urlpatterns = [
    path('', CultureListView.as_view(), name='culture_list'),
    path('<int:pk>/<slug:slug>/', CultureDetailView.as_view(), name='culture_detail'),
    path('delete/<slug:slug>/<int:pk>', CultureDeleteView.as_view(), name='culture_delete'),
    path('create/', CultureCreateView.as_view(), name='culture_create'),
    path('edit/<slug:slug>/<int:pk>/', CultureEditView.as_view(), name='culture_edit'),
]