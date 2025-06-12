from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    subjects = models.TextField()
    grades = models.TextField()
    payment_method = models.CharField(max_length=255)
    credentials = models.FileField(upload_to='credentials/')

class Lesson(models.Model):
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='lessons/videos/')
    materials = models.FileField(upload_to='lessons/materials/')
    test = models.FileField(upload_to='lessons/tests/', blank=True, null=True)
    order = models.PositiveIntegerField()
    grade = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class Subscription(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, related_name='tutor_subscriptions', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    paid_on = models.DateTimeField(auto_now_add=True)
