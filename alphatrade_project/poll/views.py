from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .forms import *
from .models import *

@login_required(login_url='login')
def home(request):
    polls = MyPoll.objects.all()

    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

@login_required(login_url='login')
def create(request):
	if request.method == 'POST':
		form = CreateMyPollForm(request.POST)
		print(form)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.author = request.user
			profile.save()
			return redirect('home')
	else:
		form = CreateMyPollForm()
	context = {
		'form' : form
	}
	return render(request, 'poll/create.html', context)

@login_required(login_url='login')
def delete(request, poll_id):
	poll = MyPoll.objects.get(pk=poll_id)
	poll.delete()
	return redirect('/profile')

@login_required(login_url='login')
def vote(request, poll_id):
    poll = MyPoll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

@login_required(login_url='login')
def results(request, poll_id):
    poll = MyPoll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)

@login_required(login_url='login')
def profile(request):
    polls = MyPoll.objects.filter(author=request.user)
    context = {
        'polls' : polls,
		'user' : request.user
    }
    return render(request, 'poll/profile.html', context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Conta criada para ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Usuário ou senha incorretos')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')