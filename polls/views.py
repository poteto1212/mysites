from django.http import HttpResponse

def index(request):
    return HttpResponse("djangoチュートリアルアプリ")
# Create your views here.
