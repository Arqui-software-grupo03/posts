from django.db import models


class Hashtag(models.Model):
    name = models.CharField(max_length=100, null=False)


class Posts(models.Model):
    content = models.CharField(max_length=400, null=False)
    pub_date = models.DateTimeField(editable=False)
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.content


class Answer(models.Model):
    author = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField(editable=False)
    post = models.ForeignKey(Posts,
                             on_delete=models.CASCADE,
                             related_name='answers'
                             )
