from django.urls import path
from ToDoapp import views

urlpatterns = [
    path('home',views.home_page),
    path('add_task',views.add_task),
    path('delete/<rid>',views.delete_task),
    path('edit/<rid>',views.edit_task),
    path('completed/<rid>',views.mark_completed),
    # path('dtl',views.dtl),
]