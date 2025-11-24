from django.urls import path
from . import views



urlpatterns = [
    path('', views.index,name="index"),
    path('<int:id>/',views.detail,name="detail"),
    path('add/',views.add_item,name='add'),
    path('update/<int:id>/',views.update_item,name='update'),
    path('delete/<int:id>/',views.delete_item,name='delete'),
   
]