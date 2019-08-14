from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadForm
from .models import Owner, Ownerdata, Campaign, Urls

def data(request):
    form = UploadForm(request.POST or None)
    if form.is_valid():
       data = form.cleaned_data['Data']
       print(data)
       load = data['data']
       response_data = {}
       response_data['data'] = load
    #    print(response_data)
       return redirect(datadisplay)
    else:
        print('invalid')
    return render(request, 'myapp/userdata.html', {'form' : form})


def datadisplay(request):
    form = Owner.objects.all()
    context = {
        'form' : form
    }
    return render(request, 'myapp/datadisplay.html', context)
