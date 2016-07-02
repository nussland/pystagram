from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='%Y/%m/%d')
    desc = models.TextField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse_lazy('photos:view_photo', kwargs={'pk':self.pk})
