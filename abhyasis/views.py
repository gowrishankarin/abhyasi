from django.http import HttpResponse

from .models import Abhyasi

# Create your views here.
def index(request):
	latest_abhyasi_list = Abhyasi.objects.order_by('-name')[:5]
	output = ', '.join([p.name for p in latest_abhyasi_list])
	return HttpResponse(output)
	
def detail(request, abhyasi_id):
	response = "You are looking at the results of question %s"
	return HttpResponse(response % abhyasi_id)

def results(request, abhyasi_id):
	return detail(request, abhyasi_id)