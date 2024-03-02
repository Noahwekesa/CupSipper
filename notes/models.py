from django.db import models
from accounts.models import CustomUser
from django_extensions.db.fields import AutoSlugField
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
