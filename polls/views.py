from django.http import HttpResponse

def index(request):
    return HttpResponse("djangoチュートリアルアプリ")
    
def detail(request,question_id):
    return HttpResponse("詳細画面" % question_id)


def results(request,question_id):
    response="質問結果の表示"
    return HttpResponse(response % question_id)
    
def vote(request,question_id):
    return HttpResponse("質問の投稿")
# Create your views here.
