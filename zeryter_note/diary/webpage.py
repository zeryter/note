from django.shortcuts import render
from diary.models import Diary
from django.contrib.auth.models import User

# Create your views here.

def homepage(request):
    diarys = Diary.objects.filter(refresh_time__isnull=False)
    user = User.objects.get(id=1)
    return render(request, 'home.html', {'diarys':diarys, 'user':user})


