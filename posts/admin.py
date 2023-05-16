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
