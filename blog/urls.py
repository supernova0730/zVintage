from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesList.as_view(), name = 'articles_list_url'),
    path('<int:id>/', views.ArticleDetail.as_view(), name = 'article_detail_url'),
    path('tag/<str:tagname>/', views.TagDetail.as_view(), name = 'tag_detail_url')
]


