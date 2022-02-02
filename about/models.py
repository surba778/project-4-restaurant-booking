from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = 'about '
        verbose_name_plural = 'about '

    def __str__(self):
        return self.title


class We_Are_Feane(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'We_Are_Feane '
        verbose_name_plural = 'We_Are_Feane '

    def __str__(self):
        return self.title
