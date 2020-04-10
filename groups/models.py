import misaka as m
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import template


User = get_user_model()

register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    descreption = models.TextField(blank=True, default='')
    descreption_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField("User", through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.descreption_html = m.html(self.descreption)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(
        "Group", related_name="membership", on_delete=models.CASCADE)
    user = models.ForeignKey(
        "User", related_name="user_groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
