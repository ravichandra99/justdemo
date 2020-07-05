from django import forms
from myapp.models import UserInfo

class SalesForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['sold']
