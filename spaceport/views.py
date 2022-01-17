
from django.shortcuts import render, redirect, reverse
import requests

def homepage(request):
    return render(request, 'index.html')