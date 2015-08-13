__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import render


def user_learning_course(request):
    return render(request, 'user/user_learning_course.html', {})
