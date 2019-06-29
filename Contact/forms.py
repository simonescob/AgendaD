# Django Contact Form 
from django import forms 

# Contact Model
from .models import Contact

# Contact Form
class ContactForm(forms.ModelForm):
  # Class 'Meta' is required for use ModelForm
  class Meta:
    model = Contact
    fields = [
      'user',
      'first_name',
      'last_name',
      'email',
      'number',
      'image',
    ]

    widgets = {
      'user': forms.Select(
        attrs={'type':'hidden'}
      )
    }
