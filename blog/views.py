from django.shortcuts import render
from django.views.generic import View

from .models import Article
from .models import Tag


class ArticlesList(View):
    def get(self, request):
        articles = Article.objects.all()
        context = {
            'articles': articles
        }
        return render(request, 'blog/articles_list.html', context)

class ArticleDetail(View):
    def get(self, request, id):
        article = Article.objects.get(id = id)
        context = {
            'article': article
        }
        return render(request, 'blog/article_detail.html', context)

class TagDetail(View):
    def get(self, request, tagname):
        tag = Tag.objects.get(name = tagname)
        articles = tag.article_set.all()
        context = {
            'tag': tag,
            'articles': articles
        }
        return render(request, 'blog/tag_detail.html', context)