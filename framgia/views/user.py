__author__ = 'FRAMGIA\le.cong.phuc'
from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm


def user_learning_course(request):
    return render(request, 'user/user_learning_course.html', {})


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return  HttpResponseRedirect("/")
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    c = {}
    c.update(csrf(request))
    return render_to_response('user/auth.html',{'state':state, 'username': username}, context_instance = RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.data['username']
            password = form.data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "user/register.html", {
        "form": form,
    })
