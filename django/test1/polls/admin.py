from django.contrib import admin

# Register your models here.

from .models import Question,Choice

# admin.site.register(Question)
admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {"fields":["question_text"]}),
        ("Date information", {"fields": ["pub_data"],"classes":["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_data']
    search_fields = ['question_text']
    list_display = ("question_text","pub_data","was_published_recently")
admin.site.register(Question,QuestionAdmin)
