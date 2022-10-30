from django.db import models
from django import forms
from django_filters import FilterSet, DateFilter, widgets
from .models import Post

class PostFilter(FilterSet):
   creation_date = DateFilter(lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}))

   class Meta:
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'article_subject': ['icontains'],
           # поиск по автору
           'author__user__username': ['icontains'],
       }
