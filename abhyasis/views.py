from django.http import Http404
from django.shortcuts import render

from .models import Abhyasi
from .forms import AbhyasiForm

# Create your views here.
def index(request):
	latest_abhyasi_list = Abhyasi.objects.order_by('-name')[:5]
	context = {	'latest_abhyasi_list': latest_abhyasi_list }
	return render(request, 'abhyasis/index.html', context)
	
def detail(request, abhyasi_id):
	try:
		abhyasi = Abhyasi.objects.get(pk=abhyasi_id)
	except Abhyasi.DoesNotExist:
		raise Http404("Abhyasi does not exist")
	return render(request, 'abhyasis/detail.html', {'abhyasi': abhyasi})

def results(request, abhyasi_id):
	return detail(request, abhyasi_id)

def abhyasi_new(request, abhyasi_id):
	form = AbhyasiForm()
	return render(request, 'abhyasis/abhyasi_edit.html', {'form': form})