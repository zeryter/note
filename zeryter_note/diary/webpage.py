from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .models import Diary
from .forms import DiaryForm

# Create your views here.

def homepage(request):
    diarys = Diary.objects.filter(refresh_time__isnull=False)
    return render(request, 'home.html', {'diarys':diarys})

def diary_views(request, pk):
    di = get_object_or_404(Diary, pk=pk)
    return render(request, 'diary_page.html', {'di': di})

def diary_new(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.auther = request.user
            diary.refresh()
            return redirect('diary.webpage.homepage')

    else:
            form = DiaryForm()
    return render(request, 'diary_edit.html', {'form':form})

def diary_edit(request, pk):
    print("test1") #TODO.......
    diary = get_object_or_404(Diary, pk=pk)
    print("test2") #TODO.......
    if request.method == "POST":
        form = DiaryForm(request.post, diary)
        diary.auther = request.user
        diary.refresh()
        return redirect('diary.webpage.homepage', pk = diary.pk)
    else:
        form = DiaryForm(instance=diary)
        return render(request, 'diary_edit.html', {'form':form})

def diary_draft(request):
    diary_drafts = Diary.objects.filter(refresh_time__isnull=True).order_by('-creat_time')
    return render(request, 'draftpage.html', {'drafts':diary_drafts})


