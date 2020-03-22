from django.db import models
class Question(models.Model):
    q=models.CharField(max_length=200)
    pub=models.DateTimeField('dtae published')
class Choice(models.Model):
    qu=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
