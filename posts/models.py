from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model
import misaka

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(
        "accounts.User", related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(
        "groups.Group", related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']
