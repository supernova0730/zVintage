from django import forms
from django.contrib import admin
from .models import Tag, Article, Reply
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    text = forms.CharField(widget = CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


admin.site.register(Tag)
admin.site.register(Reply)
admin.site.register(Article, ArticleAdmin)