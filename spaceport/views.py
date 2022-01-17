from django.shortcuts import render, redirect, reverse
import requests


# display the homepage
def homepage(request):
    return render(request, 'index.html')