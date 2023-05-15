from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# 분실물
def lost(request):
    postList = Post.objects.all()
    return render(request, 'main/lost.html', {'postList':postList})

# 푸드트럭
def foodtruck(request):
    return render(request, "main/foodtruck.html")

# 신청곡
def songRequest(request):
    return render(request, 'main/song-request.html')