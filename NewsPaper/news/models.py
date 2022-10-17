from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    rating = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(author):
        user_post_raitings = Post.objects.filter(author=author).values('rating')
        user_post_rating_sum = 0
        for user_post_raiting in user_post_raitings:
            user_post_rating_sum = user_post_rating_sum + user_post_raiting['rating']

        user_comment_raitings = Comment.objects.filter(user=author.user).values('rating')
        user_comment_rating_sum = 0
        for user_comment_raiting in user_comment_raitings:
            user_comment_rating_sum = user_comment_rating_sum + user_comment_raiting['rating']

        user_post_comment_raitings = Comment.objects.filter(post__author=author).values('rating')
        user_post_comment_rating_sum = 0
        for user_post_comment_raiting in user_post_comment_raitings:
            user_post_comment_rating_sum = user_post_comment_rating_sum + user_post_comment_raiting['rating']

        author.rating = user_post_rating_sum * 3 + user_comment_rating_sum + user_post_comment_rating_sum

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)

class Post(models.Model):
    article = 'A'
    news = 'N'

    POST_TYPE = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    type = models.CharField(max_length=1, choices=POST_TYPE, default=article)
    creation_date = models.DateTimeField(auto_now_add=True)
    article_subject = models.CharField(max_length=150)
    article_text = models.TextField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating = self.rating + 1

    def dislike(self):
        self.rating = self.rating - 1
        if self.rating < 0:
            self.rating = 0

    def preview(self):
        return self.article_text[:124] + "..."

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    comment_text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating = self.rating + 1

    def dislike(self):
        self.rating = self.rating - 1
        if self.rating < 0:
            self.rating = 0
