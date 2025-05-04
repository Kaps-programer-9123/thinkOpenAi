from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="chunking_home"),
    path("sample", views.example, name="sample_chunk"),
    path("fix_size", views.fixSize, name="fix_size_chunk"),
    path("Sliding", views.Sliding , name="Sliding_chunk"),
    path("token", views.token , name="Token_chunk"),
    path("markdown", views.markdown , name="markdown_home"),
    path("markdown/header", views.markdown_header, name="Markdown_header_chunk"),
    path("markdown/section", views.markdown_section, name="Markdown_section_chunk")
]
