from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Abhyasi, Sitting
from .forms import AbhyasiForm, SittingForm

# Create your views here.
def index(request):
	latest_abhyasi_list = Abhyasi.objects.order_by('-name')
	context = {	'latest_abhyasi_list': latest_abhyasi_list }
	return render(request, 'abhyasis/index.html', context)
	
def detail(request, abhyasi_id):
	try:
		abhyasi = Abhyasi.objects.get(pk=abhyasi_id)
		sittings = Sitting.objects.all().filter(name=abhyasi_id).order_by('-date')
	except Abhyasi.DoesNotExist:
		raise Http404("Abhyasi does not exist")
	return render(request, 'abhyasis/detail.html', {'abhyasi': abhyasi, 'sittings':sittings})

def results(request, abhyasi_id):
	return detail(request, abhyasi_id)

def abhyasi_new(request):
	print request.method
	if request.method == "POST":
		form = AbhyasiForm(request.POST)
		if form.is_valid():
			abhyasi = form.save(commit=False)
			abhyasi.save()
			return HttpResponseRedirect(reverse('abhyasis:detail', args=(abhyasi.pk,)))
		else:
			form = form
		return render(request, 'abhyasis/abhyasi_edit.html', {'form': form})
	else:
		form = AbhyasiForm()
		return render(request, 'abhyasis/abhyasi_edit.html', {'form': form})

def abhyasi_edit(request, pk):
	abhyasi = get_object_or_404(Abhyasi, pk=pk)
	if request.method == "POST":
		form = AbhyasiForm(request.POST, instance=abhyasi)
		if form.is_valid():
			abhyasi = form.save(commit=False)
			abhyasi.save()
			return HttpResponseRedirect(reverse('abhyasis:detail', args=(abhyasi.pk,)))
		else:
			form = form
		return render(request, 'abhyasis/abhyasi_edit.html', {'form': form})
	else:
		form = AbhyasiForm(instance=abhyasi)
	return render(request, 'abhyasis/abhyasi_edit.html', {'form':form})

def sitting_new(request, pk):
	abhyasi = get_object_or_404(Abhyasi, pk=pk)
	if request.method == "POST":
		form = SittingForm(request.POST)
		if form.is_valid():
			sitting = form.save(commit=False)
			sitting.name_id = pk
			sitting.save()
			return HttpResponseRedirect(reverse('abhyasis:detail', args=(abhyasi.pk,)))
		else:
			form = form
		return render(request, 'abhyasis/sitting_new.html', {'form': form, 'abhyasi':abhyasi})
	else:
		form = SittingForm()
	return render(request, 'abhyasis/sitting_new.html', {'form': form, 'abhyasi':abhyasi})	
