__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import render


def index(request):
    return render(request, 'course/index.html', {})



