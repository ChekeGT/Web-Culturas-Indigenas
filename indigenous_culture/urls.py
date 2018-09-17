from django.urls import  path
from .views import CultureListView, CultureDetailView, DictDetailView, DictResponse

urlpatterns = [
    path('', CultureListView.as_view(), name='culture_list'),
    path('<int:pk>/<slug:slug>/', CultureDetailView.as_view(), name='culture_detail'),
    path('dict/<int:pk>/', DictDetailView.as_view(), name='dict_detail'),
    path('dict/<int:pk>/translate', DictResponse, name='translate')
]