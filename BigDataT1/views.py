import pathlib
import textwrap

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

def index(request):
   # data = FILES_CHOICES
    data = []
    currentDirectory = pathlib.Path('Reuters')

    for currentFile in currentDirectory.iterdir():
        data.append({'name': currentFile.name})
   #   for name in sorted(data, key='name'):
        #        print("{} --> {}".format(name, data[name]))

    return render(request, "index.html", {'data': data})