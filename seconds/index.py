from django.shortcuts import render
from django.http import HttpResponse, Http404

"""
The view for rendering the index page
"""
def indexView(request):
    output = "oof"
    return HttpResponse(output)