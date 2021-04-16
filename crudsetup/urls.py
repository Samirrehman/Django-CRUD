from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('addbook/',views.addbook,name="addbook"),
    path('create/',views.create,name="create"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
]
