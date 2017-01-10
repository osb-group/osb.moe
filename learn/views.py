from django.shortcuts import render
from sphinx.websupport.errors import DocumentNotFoundError
from django.http import Http404, HttpResponseBadRequest
from _variables import support
import logging

# region Requests


def get_document(request, document_path):
    logger = logging.getLogger(__name__)
    try:
        contents = support.get_document(document_path)
        return render(request, 'learn/document.html', contents)
    except DocumentNotFoundError:
        logger.error("The path: '{0}' was unable to be found. Hence, Http404 error".format(document_path))
        raise Http404
    except:
        logger.error("The path: '{0}' seemed to have found an error somewhere.".format(document_path))
        raise

# endregion
