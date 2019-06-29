from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'password',
		]
		widgets = {
			"password": forms.PasswordInput(),
		}

		def clean_password2(self):
			password = self.request.POST['password']
			password2 = self.request.POST['password2']
			if password != password2:
				raise forms.ValidationError("¡Las claves no coinciden!")
			return password2
