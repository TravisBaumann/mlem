from django.contrib import admin

# Register your models here.
from .models import TwitterPosts, Profile

class TwitterPostsAdmin(admin.ModelAdmin):
	list_display = ('user', 'twitter_posts', 'date', )

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(TwitterPosts, TwitterPostsAdmin)
admin.site.register(Profile)
