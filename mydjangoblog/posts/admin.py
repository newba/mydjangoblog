from django.contrib import admin

# Register your models here.
#https://docs.djangoproject.com/en/1.11/ref/contrib/admin/

from.models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ["_str_", "data"]
    list_filter = ["data"]
    search_fields = ["titulo", "conteudo"]
    prepopulated_fields = {"slug": ("titulo",)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)