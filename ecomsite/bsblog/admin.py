from django.contrib import admin
from .models import Post
admin.autodiscover()

admin.site.register(Post)

