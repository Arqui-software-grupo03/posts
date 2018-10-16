from django.db import models


class Posts(models.Model):
    content = models.CharField(max_length=400, null=False)

    def __str__(self):
        return self.content

class Hashtag(models.Model):
    post = models.ForeignKey(
        Posts,
        related_name='hashtags',
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return '#' + self.name
