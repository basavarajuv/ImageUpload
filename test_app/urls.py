from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.image_upload, name='image upload'),
    path('show_images', views.show_images, name='show images'),
    path('test', views.test_example, name='test example'),

]
