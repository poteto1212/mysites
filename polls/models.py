from django.db import models
#時刻モジュールインポート
import datetime
from django.utils import timezone

#投稿用ﾓﾃﾞﾙ
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    
    
#質問用ﾓﾃﾞﾙ    
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text



# Create your models here.
