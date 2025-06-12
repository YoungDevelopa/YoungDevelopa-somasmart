from django.contrib import admin
from .models import User, TutorProfile, Lesson, Subscription

admin.site.register(User)
admin.site.register(TutorProfile)
admin.site.register(Lesson)
admin.site.register(Subscription)
