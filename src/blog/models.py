from django.db import models

# Create your models here.


class BlogPost(models.Model):
    # id = models.IntegerField() pk
    title = models.TextField()
    slug = models.SlugField(unique=True)  # hello wold -> hello-wolrd
    content = models.TextField(null=True, blank=True)
