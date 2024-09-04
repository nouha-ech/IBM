from django.shortcuts import render

# Create your views here.

def form_view(request):   # create a view function to render the form.html template
    return render(request, 'form.html')