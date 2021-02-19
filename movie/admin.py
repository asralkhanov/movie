from django.contrib import admin
from .models import *
from django import forms

from django.utils.html import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
class ReviewsInline(admin.TabularInline):#admin.StackedInline
    model = Reviews
    extra = 1
    readonly_fields = ('name','email')

class MovieShotsInline(admin.TabularInline):
    model = Movie_Shots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='200' height='200'>")

    get_image.short_description = 'Filmdan kadr'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    desc = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    list_display = ('title', 'category',)
    list_display_links = ('title',)
    list_filter = ('country', 'category')
    search_fields = ('title', 'category__name',)
    prepopulated_fields = {'slug':('title',)}
    inlines = [ReviewsInline, MovieShotsInline]
    save_on_top = True
    save_as =True

    
    # fieldsets = (
    #    ( None, {
    #         'fields':(('title', 'tagline'), )
    #    }
    #     ),
    # )
    # fields = (('actors','genres'),)
    # list_editable = ('year',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    list_display_links = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'get_image')
    list_filter = ('name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='100' height='100'>")

    get_image.short_description = 'Aktyor rasmi'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(Movie_Shots)
class MovieshotsAdmin(admin.ModelAdmin):
    list_display = ('movie',)
    list_filter = ('title',)


@admin.register(Directors)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'age')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    readonly_fields = ('name', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'author', 'published', 'views')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(RatingStar)

admin.site.register(Rating)


admin.site.site_title = "Django Movies"
admin.site.site_header = "Django Movies"