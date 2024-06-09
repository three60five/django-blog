from django.contrib import admin
from blogging.models import Post

# and a new admin registration
admin.site.register(Post)
