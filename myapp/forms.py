from django import forms
from .models import Owner#, Ownerdata, Campaign, Urls



class UploadForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['Data'] 
       

# class OwnerForm(forms.ModelForm):
#     class Meta:
#         model = Ownerdata

# class CampaigndForm(forms.ModelForm):
#     class Meta:
#         model = Campaign

# class UrlsForm(forms.ModelForm):
#     class Meta:
#         model = Urls