from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse

from django.views.generic import (
    ListView, DetailView
)

from .models import Article
from .models import Tag
from .models import Reply
from .forms import ReplyForm


class ArticlesList(ListView):
    queryset = Article.objects.all()
    template_name = 'blog/articles_list.html'


class ArticleDetail(View):
    def get(self, request, id):
        article = Article.objects.get(id = id)
        form = ReplyForm()
        context = {
            'article': article,
            'form': form
        }
        return render(request, 'blog/article_detail.html', context)
    
    def post(self, request, id):
        form = ReplyForm(request.POST)
        article = Article.objects.get(id = id)
        if form.is_valid():
            form.save(commit = False)
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            reply = Reply(
                email = email, 
                name = name, 
                content = content, 
                article = article
            )
            reply.save()
            return redirect(article.get_absolute_url())


class TagDetail(View):
    def get(self, request, tagname):
        tag = Tag.objects.get(name = tagname)
        articles = tag.article_set.all()
        context = {
            'tag': tag,
            'object_list': articles
        }
        return render(request, 'blog/tag_detail.html', context)


