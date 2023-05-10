from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib import messages
from .management.commands.startvoting import vote_instance
from asgiref.sync import async_to_sync

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vote')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def vote(request):
    if request.method == 'POST':
        votes = ['vim', 'emacs', 'vscode', 'nano']
        choice = request.POST['editor'].lower()
        user = request.user
        voter = user.voter.voter
        voter.vote(votes.index(choice))
        vote_instance.add_vote(voter)

    return render(request, 'accounts/vote.html')

@user_passes_test(lambda u : u.is_superuser)
@async_to_sync
async def result(request):
    if request.method == 'POST':
        votes = ['vim', 'emacs', 'vscode', 'nano']
        result = await vote_instance.get_result();
        display = list(map(lambda t: (votes[t[0]], t[1]), sorted(result, key=lambda t: t[1], reverse=True)))
        display = {t[0] : t[1] for t in display}
        context = { 'result': display }
    else:
        context = {}

    return render(request, 'accounts/result.html', context)
