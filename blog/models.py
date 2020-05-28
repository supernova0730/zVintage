from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs = { 'tagname' : self.name })

class Article(models.Model):
    title = models.CharField(max_length = 255)
    min_text = models.CharField(max_length = 1023, blank = True, default="")
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'images', null = True, blank = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs = { 'id' : self.id })

class Reply(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length = 255)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    date_created = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.content
    
