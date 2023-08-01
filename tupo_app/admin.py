from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html,strip_tags
from .models import *

# admin.site.register(CustomUser, UserAdmin)



@admin.register(AboutUsModel) 
class AboutUsModel(admin.ModelAdmin):

    list_display = [
            'name',
            'about_content',
            'created_at',
            'modified_at',
        ]

@admin.register(CreditModel) 
class CreditModel(admin.ModelAdmin):

    def get_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.img.url))

    get_img.short_description = 'Credit'

    list_display = [
            'name',
            'img',
            'content',
            'created_at',
            'modified_at',
        ]

@admin.register(Award) 
class Award(admin.ModelAdmin):

    def get_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.img.url))

    get_img.short_description = 'Credit'

    list_display = [
            'name',
            'img',
            'content',
            'created_at',
            'modified_at',
        ]
@admin.register(Nomination) 
class Nomination(admin.ModelAdmin):

    list_display = [
            'title',
            'first_name',
            'last_name',
            'position',
            'birthday',
            'city',
            'state',
            'email',
            'created_at',
            'modified_at',
        ]
@admin.register(Emytology)  
class Emytology(admin.ModelAdmin):

    list_display = [
            'name',
            'created_at',
            'modified_at',
    ]

@admin.register(Community)  
class Community(admin.ModelAdmin):
    def get_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.img.url))

    list_display = [
            'title',
            'name',
            'img',
            'created_at',
            'modified_at',
        ]
    
@admin.register(CommunityArticle)  
class CommunityArticle(admin.ModelAdmin):
    def get_img(self, obj):
        return format_html('<img src="{}" width="100" />'.format(obj.img.url))

    list_display = [
            'title',
            'img',
            'created_at',
            'modified_at',
        ]