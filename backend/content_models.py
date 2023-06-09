from django.db import models
from django.contrib.auth.models import User
from .models import Client

class Content(models.Model):
    BLOG = 1
    WEBINAR = 2
    VIDEO = 3

    CONTENT_TYPES = (
        (BLOG, "Blog"),
        (WEBINAR, "Webinar"),
        (VIDEO, "Video"),
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    instructor = models.ForeignKey(User, related_name="Instructor", on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.CharField(max_length=50, default="0")
    type = models.IntegerField(choices=CONTENT_TYPES)
    tier_access = models.JSONField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    text = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ContentActivity(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    times_viewed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PrivateSession(models.Model):
    ACTIVE = 1
    RESCHEDULED = 2
    CANCELLED = 3
    PENDING = 4

    SESSION_STATUS = (
        (ACTIVE, "Active"),
        (RESCHEDULED, "Rescheduled"),
        (PENDING, "Pending"),
        (CANCELLED, "Cancelled"),
    )

    meeting_url = models.URLField()
    status = models.IntegerField(choices=SESSION_STATUS, default=PENDING)
    instructor = models.ForeignKey(User, related_name="Instructor", on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, related_name="Job seeker", on_delete=models.CASCADE)
    schedule_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)