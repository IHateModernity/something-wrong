import datetime
from sqlite3 import IntegrityError

from django.db import models

# Create your models here.
from django.utils.text import slugify


class Post(models.Model):

    title = models.CharField('Title', blank=False, max_length=56, default=None)
    description = models.CharField('Description', blank=False, max_length=512, default=None)
    author = models.CharField('Author\'s name', max_length=56, blank=False, default='Anonymous')
    image = models.ImageField('Image', max_length=56, blank=False, default="Noimage.png")
    created_date = models.DateTimeField(blank=True, default=datetime.datetime.now)
    slug = models.SlugField('Slug', max_length=56, unique=False)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify([self.title])
        super(Post, self).save(**kwargs)

    def get_absolute_url(self):
        return f"/project/{self.slug}/{self.id}"
