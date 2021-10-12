from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Genre(models.Model):
    genre=models.CharField(max_length=100)
    created_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title=models.CharField(max_length=200,unique=True)
    author_name=models.ForeignKey(User,on_delete=models.CASCADE)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.author_name)

    def get_absolute_url(self):
        return reverse('post_detail',args=(str(self.id)))
