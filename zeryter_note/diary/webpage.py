from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Diary
from .forms import DiaryForm


# 主页，所有文章列表
def homepage(request):
    diarys = Diary.objects.filter(refresh_time__isnull=False)
    return render(request, 'home.html', {'diarys': diarys})


# 文章详情
def diary_views(request, pk):
    di = get_object_or_404(Diary, pk=pk)
    return render(request, 'diary_page.html', {'di': di})


# 新建文章
def diary_new(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        checkbox_list = request.REQUEST.getlist('diary')
        if form.is_valid():
            diary = form.save(commit=False)
            diary.auther = User.objects.get(id=2)
            print(form)
            print(checkbox_list)
            diary.auther = request.user  # TODO这里需要登录功能处理
            if checkbox_list and checkbox_list[0] == '草稿箱':
                diary.save()
                return redirect('diary.webpage.diary_draft')
            diary.refresh()
            return redirect('diary.webpage.homepage')
    else:
        form = DiaryForm
    return render(request, 'diary_edit.html', {'form': form})


# 内容编辑
def diary_edit(request, pk):
    diary = get_object_or_404(Diary, pk=pk)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            # diary.auther = request.user
            diary.auther = User.objects.get(id=2)
            diary.save()
        return redirect('diary.webpage.homepage', pk=diary.pk)
    else:
        form = DiaryForm(instance=diary)
    return render(request, 'diary_edit.html', {'form': form})


# 草稿箱列表
def diary_draft(request):
    diary_drafts = Diary.objects.filter(refresh_time__isnull=True).order_by('-creat_time')
    return render(request, 'draftpage.html', {'drafts': diary_drafts})


# 草稿箱发布功能
def diary_publish(pk):
    diary = get_object_or_404(Diary, pk=pk)
    diary.refresh()
    return redirect('diary.webpage.homepage')
