from django.urls import path
from .views import all_todo, update, create,delete

urlpatterns = [
    path('', all_todo, name='all_todo'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
