from django.urls import path

from . import  views

app_name = 'todo'

urlpatterns = [
    path('',views.home,name='home'),
    path('todo_list/',views.todo_list,name='todo_list'),
    path('todo_item/<int:todo_id>',views.todo_item,name='todo_item'),
]