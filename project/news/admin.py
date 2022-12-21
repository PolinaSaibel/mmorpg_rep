from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Response, Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "time_creation"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["user"]


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ["author", "post", "time_creation", "status"]
