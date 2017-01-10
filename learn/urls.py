from django.conf.urls import url
from .views import get_document

urlpatterns = [
    url(r'(?P<document_path>.+)/$', get_document)
]