from django.shortcuts import render
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
    else:
        print('invalid')
    return render(request, 'myapp/userdata.html', {'form' : form})



