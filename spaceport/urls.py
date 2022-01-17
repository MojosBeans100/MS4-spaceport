from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create_pipeline.html', views.create, name='create'),
    path('save.html', views.save, name='save'),
    path('my_pipelines.html', views.my_pipelines, name='my_pipelines'),
    #path('detail_view/<int:id>',views.detail_view,name='detail_view'),
]