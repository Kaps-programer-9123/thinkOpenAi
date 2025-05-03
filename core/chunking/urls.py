from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="chunking_home"),
    path("sample", views.example, name="sample_chunk"),
    path("fix_size", views.fixSize, name="fix_size_chunk"),
    path("Sliding", views.Sliding , name="Sliding_chunk")
]
