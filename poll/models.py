from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    title=models.CharField("Название опроса", max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)
    end_date=models.DateField('Дата окончания опроса',null=True)
    description= models.CharField("Описание", max_length=150,null=True)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('poll', kwargs={'poll_id': self.pk})


class Question(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    question= models.CharField('Вопрос',max_length=150)
    types = (
        ('Ответ текстом', 'Ответ текстом'),
        ('Ответ с выбором одного варианта', 'Ответ с выбором одного варианта'),
        ('Ответ с выбором нескольких вариантов', 'Ответ с выбором нескольких вариантов')
    )
    type = models.CharField('Условие',max_length=50, choices=types, null=True)

    def get_absolute_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField('Ответ',max_length=60)
    def __str__(self):
        return self.answer

class ResultsModel(models.Model):
    user = models.CharField(max_length=100)
    answer=models.CharField('Ваш ответ',max_length=100)
    question=models.CharField(max_length=100)



