from django.shortcuts import render
from gra.models import Game


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm






# Create your views here.

def games(request):
    return render(request, 'games.html', {'games': Game.objects.all()})


# def game(request):
#    return render(request,'game.html',{'games' : Game.objects(id=1)})


# def game(request, id):
#   return render(request, 'game.html', {'user_id': id})


#def game(request, game_id):
#   return render(request, 'game.html', {'games_id': Game.objects.get(id=1)})

def game1(request):
    return render(request, 'game.html', {'game': Game.objects.get(id=1)})

def game2(request):
    return render(request, 'flapy.html')

def game3(request):
    return render(request, 'obrazki.html')

def main(request):
	return render(request,'main.html')

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')


def loggedin(request):
	return render(request,'loggedin.html',{'user_name' : request.user.username})




def logout(request):
    auth.logout(request)
    return render(request,'logout.html')



def invalid_login(request):
	return render(request,'invalid_login.html')


def create_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/create_user_success/')

	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()

	return render(request,'create_user.html', args)

def create_user_success(request):
	return render(request,'create_user_success.html')
