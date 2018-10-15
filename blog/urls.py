from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/show',views.show,name='show'),
    #访问localhost:8003/blog/1/show这个页面，1：文章ID
]