from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def file_upload(request):
    return HttpResponse("<strong><em>Upload your file here</em></strong>")