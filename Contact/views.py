# Contact View.py

# Django Libraries
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

# Contact Model
from .models import Contact

# Contact Form
from .forms import ContactForm

# Function Index for display contacts
def index(request):
	user = request.user
	contacts = Contact.objects.filter(user=user)
	return render(request, "contact/index.html", 
		{
			"contacts": contacts,
			"user": user,
		} 
	)

# Class Based View for create a Contact
class ContactCreate(CreateView):	
	model = Contact
	fields = [
		'user',
		'first_name',
		'last_name',
		'number',
		'email',
		'image',
	]
	template_name = 'contact/create.html'
	success_url = reverse_lazy('contact:index')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		return context

class ContactDelete(DeleteView):
	model = Contact
	template_name = 'contact/delete.html'
	success_url = reverse_lazy('contact:index')
	slug_field = 'id'
	slug_url_kwarg = 'id'

class ContactUpdate(UpdateView):
	model = Contact
	fields = [
		'first_name',
		'last_name',
		'number',
		'email',
		'image',
	]
	template_name = "contact/update.html"
	success_url = reverse_lazy('contact:index')
	slug_field = 'id'
	slug_url_kwarg = 'id'