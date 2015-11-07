from django.shortcuts import render, get_object_or_404
from .models import Diary

# Create your views here.

def homepage(request):
    diarys = Diary.objects.filter(refresh_time__isnull=False)
    return render(request, 'home.html', {'diarys':diarys})

def diary_views(request, pk):
    di = get_object_or_404(Diary, pk=pk)
    return render(request, 'diary_page.html', {'di': di})


