from django.db import models

class NnaUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

class NnaCategory(models.Model):
    name = models.CharField(max_length=100)

class NnaFAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(NnaCategory, on_delete=models.CASCADE)
