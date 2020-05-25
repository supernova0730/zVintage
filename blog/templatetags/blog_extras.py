from django import template
from blog.models import Tag
from blog.models import Article
from random import randint

register = template.Library()

@register.simple_tag
def get_tags():
    tags = Tag.objects.all()
    return tags

@register.simple_tag
def get_last_posts():
    posts = Article.objects.order_by('-date_created')[:4]
    return posts