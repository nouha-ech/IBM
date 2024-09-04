from django.shortcuts import render
from . models import Provider

# Create your views here.

def form_view(request):   # create a view function to render the form.html template
    return render(request, 'form.html')

def provider_list(request):  # view func to render the providers_list.html template
    
    providers = Provider.objects.all()    # get all the providers from the database
    return render(request, 'provider_list.html', {'providers': providers})