from django.shortcuts import render
from .models import *


def main(request):
    studies = Study.objects.all()
    ctx = {
        'studies': studies
    }
    return render(request, 'main.html', ctx)
