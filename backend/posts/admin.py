from django.contrib import admin

from . import models


@admin.display(description='Short Text')
def get_short_text(obj):
    return f'{obj.text[:10]}...'


class TweetImagesInline(admin.TabularInline):
    model = models.TweetImages
    extra = 1


@admin.register(models.Tweet)
class TweetAdmin(admin.ModelAdmin):
    inlines = [
        TweetImagesInline
    ]
    list_display = ['id', 'get_profile_fullname', get_short_text, 'get_reactions_str', 'image', 'created_at']
    date_hierarchy = 'created_at'
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = '--empty--'
    # exclude = ['profile', 'image']
    # fields = ['text']
    fields = (('text', 'profile'), 'image')
    list_display_links = [get_short_text]
    list_editable = ['image', ]
    list_filter = ['created_at', 'profile']
    list_per_page = 2
    save_as = True
    search_fields = ['text', 'profile__user__username']
    sortable_by = ['created_at', 'id']

    @admin.display(description='Fullname')
    def get_profile_fullname(self, obj):
        return obj.profile.user.get_full_name()


@admin.register(models.Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ['tweet', 'profile', 'reaction']


@admin.register(models.ReactionType)
class ReactionTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'get_fullname', 'get_short_text', 'created_at', 'get_reactions_str', 'get_tweet_id']
    date_hierarchy = 'created_at'
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = '-'
    fields = (('text', 'profile'), 'tweet')
    list_display_links = ['get_short_text', ]
    list_editable = ['profile']
    search_fields = ['text', 'profile__user__first_name', 'profile__user__last_name']
    sortable_by = ['id', 'created_at']

    @admin.display(description='Fullname')
    def get_fullname(self, obj):
        return obj.profile.user.get_full_name()

    @admin.display(description='Short text')
    def get_short_text(self, obj):
        return f'{obj.text[:20]}...'

    @admin.display(description='Tweet id')
    def get_tweet_id(self, obj):
        return obj.tweet.id