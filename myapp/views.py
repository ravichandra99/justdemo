from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from myapp.forms import SalesForm
from django.http import HttpResponseRedirect
from myapp.models import UserInfo,UserMaster
from django.contrib.auth import logout


@login_required
def index(request):
    print('im in index')
    try:
        usermaster_id = User.objects.get(id = request.user.id).id
        userinfo_id = UserMaster.objects.get(user_id = usermaster_id).id
    except:
        return render(request,'notfound.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SalesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            sold = form.cleaned_data['sold']
            u = UserInfo.objects.get(user_id = userinfo_id)
            u.sold = sold
            u.remaining = u.total - u.sold
            u.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('myapp:index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SalesForm()

    print(usermaster_id,userinfo_id)
    if UserMaster.objects.filter(user_id = usermaster_id).exists() and UserInfo.objects.filter(user_id = userinfo_id).exists():
        
        detail = UserInfo.objects.filter(user_id = userinfo_id)
        print(detail)

        return render(request, 'index.html', {'form': form,'detail':[i for i in detail]})
    else:
        return render(request,'notfound.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('myapp:index')


