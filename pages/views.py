from django.shortcuts import render


# Create your views here.

def home(request, *args, **kwargs):
    
    return render(request, 'home.htm', {})
	
def about(request, *args, **kwargs):
    
    return render(request, 'about.htm', {})
	
def service(request, *args, **kwargs):
    
    return render(request, 'service.htm', {})
	
	
def team(request, *args, **kwargs):
    
    return render(request, 'team.html', {})

	
def contact(request, *args, **kwargs):
    
    return render(request, 'contact.htm', {})
	
def potfolio(request, *args, **kwargs):
    
    return render(request, 'potfolio', {})
	
def clients(request, *args, **kwargs):
    
    return render(request, 'client', {})
	
def faq(request, *args, **kwargs):
    
    return render(request, 'faq', {})
