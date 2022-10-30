from django.urls import path
# Импортируем созданные нами представления
from .views import (
   NewsList, NewsDetail, SearchList, NewsPostCreate, NewsPostUpdate, NewsPostDelete,
   ArticlePostCreate, ArticlePostUpdate, ArticlePostDelete
)

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', NewsList.as_view(), name='news_list'),
   # pk — это первичный ключ новости, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
   path('search', SearchList.as_view(), name='searh_news_list'),

   path('news/create/', NewsPostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit', NewsPostUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete', NewsPostDelete.as_view(), name='news_delete'),

   path('articles/create/', ArticlePostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit', ArticlePostUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete', ArticlePostDelete.as_view(), name='articles_delete'),

]
