from django.db import models
from django.forms import ImageField

# Create your models here.
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class Post(models.Model):
    """Model definition for Post."""

    author = models.ForeignKey(User, verbose_name=_("author"), on_delete=models.CASCADE)
    image = models.ImageField(_("post image "), upload_to='post/', blank=True , null=True)
    caption = models.TextField(_("caption"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Unicode representation of Post."""
        return str(self.caption)
