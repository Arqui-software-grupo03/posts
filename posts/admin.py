from django.contrib import admin
from .models import Posts, Hashtag


admin.site.register([Posts, Hashtag])
