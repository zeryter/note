from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone

# Create your models here.

class Diary(models.Model):
    '''
    创建 ‘日记(diary)’ 的models
    拥有的字段：
            auther：日记作者
            creat_time：创建日记时间
            refresh_time：提交时间
            text: 内容
            title: 题目（如果需要的话）
            后期添加：
                    天气
                    心情
                    想法
                    状态
    '''
    auther = models.ForeignKey(User)
    creat_time = models.DateTimeField(default=timezone.now())
    refresh_time =  models.DateTimeField(null=True, blank=True)
    title =  models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=20000)

    def refresh(self):
         self.refresh_time = timezone.now()
         self.save()

    def __str__(self):
        if self.title:
            return '日记题目' +str(self.title)
        else:
            return '日记创建时间' + str(self.creat_time)
