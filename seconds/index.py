from django.shortcuts import render
from django.http import HttpResponse, Http404

from game.version import getVersion

"""
The view for rendering the index page
"""
def indexView(request):
    version = getVersion()
    return render(request, 'game/index.html', {'version': version})