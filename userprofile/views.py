from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from userprofile.forms import UsersProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def userprofile(request):
    if request.method == 'POST':
        form = UsersProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/loggedin/')

    else:
        user = request.user
        profile = user.profile
        form = UsersProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))
    args['form']=form

    return render(request,'user_profile.html',args)


