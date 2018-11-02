from django.contrib import admin
from .models import Posts, Hashtag, Answer


admin.site.register([Posts, Hashtag, Answer])
