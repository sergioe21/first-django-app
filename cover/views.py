from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def show(request):

	data = Person.objects.all()
	if len(data) > 0:
		return render(request, 'cover/cvr.html',{'person': data[0]})
	else:
		return render(request, 'cover/empty.html',{})


