from django.urls import  path
from .views import *
urlpatterns = [
    path('dict/<int:pk>/', DictDetailView.as_view(), name='dict_detail'),
    path('dict/<int:pk>/translate', DictResponse, name='translate'),
    path('dict/edit/<int:pk>', WordsCreateView.as_view(), name='dict_add'),
    path('dict/edit/response/<int:pk>', DictEditResponse, name='dict_add_response'),
    path('word/list/<int:pk>/', WordListView.as_view(), name='word_list'),
    path('word/edit/<int:pk>/', WordEditView.as_view(), name='word_edit'),
    path('word/delete/<int:pk>', WordsDeleteView.as_view(), name='word_delete'),
    path('word/edit_or_delete/response/<int:pk>', WordEditOrDeleteResponse, name='word_edit_or_delete_response'),
]