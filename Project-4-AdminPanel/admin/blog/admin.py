from django.contrib import admin
from blog.models import Blog  # import Model Class
from articles.models import Article

admin.site.register(Blog)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","author")


admin.site.register(Article,ArticleAdmin)

