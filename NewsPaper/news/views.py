from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        context['breaking_news'] = 'Скоро срочное сообщение!!!'
        return context

class SearchList(NewsList):
    template_name = 'search.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
       # Получаем обычный запрос
       queryset = super().get_queryset()
       # Используем наш класс фильтрации.
       # self.request.GET содержит объект QueryDict, который мы рассматривали
       # в этом юните ранее.
       # Сохраняем нашу фильтрацию в объекте класса,
       # чтобы потом добавить в контекст и использовать в шаблоне.
       self.filterset = PostFilter(self.request.GET, queryset)
       # Возвращаем из функции отфильтрованный список товаров
       return self.filterset.qs

class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = Post
    template_name = 'detail.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'detail'
