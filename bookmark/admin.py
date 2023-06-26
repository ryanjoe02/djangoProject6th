from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.

# not using decorator
# admin.site.register(Bookmark, BookmarkAdmin):
@admin.register(Bookmark)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
