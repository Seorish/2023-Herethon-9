from django.db import models
from django.utils import timezone
from enum import Enum

# 카테고리
class category(Enum):
    위험 = '위험'
    추행 = '추행'
    폭행 = '폭행'
    침입 = '침입'

# 글 생성
class Post(models.Model):
    title = models.CharField(max_length=50)
  #  author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=[(status.value, status.name) for status in category])


class Comment(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
