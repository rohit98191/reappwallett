from django.contrib import admin
from .models import Question,Choice


class ChoiceIn(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    inlines = [ChoiceIn]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    list_per_page = 1
    search_fields = ['question_text']




admin.site.register(Question,QuestionAdmin)

