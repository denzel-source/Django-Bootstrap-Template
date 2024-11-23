from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='my_index'),

    path('blog/', views.blog, name='my_blog'),
    path('appointment/', views.appointment, name='my_appointment'),
]