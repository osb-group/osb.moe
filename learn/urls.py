from django.conf.urls import url
from .views import get_document, search_request

urlpatterns = [
    url(r'search', search_request),
    url(r'(?P<document_path>.+)/$', get_document),
]