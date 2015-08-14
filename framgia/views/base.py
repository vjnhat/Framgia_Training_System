__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'index.html', context)

