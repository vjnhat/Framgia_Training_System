__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import HttpResponse, render
from django.views.generic import ListView, DetailView, View


class Home(View):
    def get(self, request):
        return render(request,'index.html')
