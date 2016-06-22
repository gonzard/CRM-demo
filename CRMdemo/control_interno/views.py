from django.shortcuts import render
from control_interno.forms import AddClientForm
from django.http import HttpResponseRedirect


# Create your views here.


def control_interno(request):
	return render(request, 'add_client.html')

def add_client(request):
	form = AddClientForm()
	if request.method == 'POST':
		form = AddClientForm(request.POST or None)
        if form.is_valid():
        	post = form.save(commit=False)
        	post.save()
        	return HttpResponseRedirect('/')
	return render(request, 'add_client.html', {'form': form})
