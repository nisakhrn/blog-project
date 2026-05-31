from django.db import models


class Article(models.Model):

    title = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to='articles/',
        blank=True,
        null=True
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title