
from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.translation import gettext as _
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("username"), on_delete=models.CASCADE ,blank=True, null=True)
    image = models.ImageField(_("image"), upload_to='profile_pics/')
    bio = models.TextField(_("bio") ,blank=True, null=True)
    posts = models.ForeignKey("Post", verbose_name=_("posts"), related_name='profile_posts', on_delete=models.CASCADE)
    # folowers 
    # following 
    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.user.username



class Post(models.Model):
    title=models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, verbose_name=_("profile"), related_name='post_profile', on_delete=models.CASCADE)
    username = models.CharField(_("username"), max_length=150)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130, blank=True, null=True)
    caption = models.TextField(_("caption"))
    image = models.ImageField(upload_to="post_pics/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post , self).save(*args, **kwargs)

