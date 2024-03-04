from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
   return render(request, 'shop/home.html')

def register(request):
   if request.POST == 'POST':
      form = UserCreationForm()
      if form.is_valid():
         form.save()
      messages.succes(request, 'Account created successfully!')
   else:
      form = UserCreationForm()
   context = {
      'form': form,
   }
   return render(request, 'register.html', context)
def loginView(request):
   return render(request, 'login.html')