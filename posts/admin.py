from django.contrib import admin
from .models import Post
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title','updated','created']
	list_display_links = ['updated']
	list_editable = ['title']
	list_filter = ['updated','title','created']
	search_fields = ['title']
	class Meta:
		model = Post


admin.site.register(Post,PostModelAdmin)