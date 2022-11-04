from django.contrib import admin

from exam.models import Contact, Demo, English, Essay, Maths, Score


# Register your models here.

admin.site.register(Contact)
admin.site.register(Maths)
admin.site.register(English)
admin.site.register(Score)
admin.site.register(Demo)
admin.site.register(Essay)
