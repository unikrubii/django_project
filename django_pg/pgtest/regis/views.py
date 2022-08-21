from django.shortcuts import render
from .models import User

# Create your views here.
def regis(request):
	return render(request, 'register.html', {"text": "You are welcome to register."})

def index(request):
	return render(request, 'index.html', {"text": "You are welcome to look around."})

def addData(request):
	if request.method == "POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		
		payload = {
			"firstname": firstname,
			"lastname": lastname,
			"email": email,
		}
		user = User(
			firstname = firstname.capitalize(),
			lastname = lastname.capitalize(),
			email = email.lower(),
		)
		user.save()

	return render(request, 'result.html', payload)
