from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(User):
    phone_number = models.IntegerField()
    address = models.CharField(max_length=50, null=True, blank=True)
    profile_image = models.ImageField(upload_to="images/", default='user.png')
    date_of_birth = models.DateField(null=True, blank=True)
    is_online = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Membership(models.Model):
    name = models.CharField(max_length=250)
    description = models.JSONField(null=False, blank=False)
    price = models.FloatField()
    tier = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClientMembership(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    auto_renewal = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Query(models.Model):
    text = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=250)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    instructor = models.ForeignKey(User, related_name="Admin", on_delete=models.SET_NULL, null=True, blank=True)
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
        (CANCELLED, "Cancelled"),
        (PENDING, "Pending"),
    )

    meeting_url = models.URLField()
    status = models.IntegerField(choices=SESSION_STATUS, default=PENDING)
    instructor = models.ForeignKey(User, related_name="Instructor", on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(Client, related_name="JobSeeker", on_delete=models.CASCADE)
    schedule_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meeting_url

    @property
    def status_color(self):
        if self.status == self.CANCELLED:
            return 'bg-danger-light text-danger-dark'
        if self.status == self.ACTIVE:
            return 'bg-main-light text-main'
        return 'bg-accent-light text-accent-dark'

    @property
    def status_text(self):
        return self.SESSION_STATUS[self.status-1][1]

    # class PaymentMethod(models.Model):
    #
    #     client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #     card_holder_name = models.CharField(max_length=250)
    #     card_holder_number = models.CharField(max_length=100)
    #     expiration_date = models.CharField(max_length=10)
    #     security_code = models.CharField(max_length=10)
    #     created_at = models.DateTimeField(auto_now_add=True)
    #     updated_at = models.DateTimeField(auto_now=True)


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=50)
    coupon_discount = models.FloatField()  # Percentage
    expiration_date = models.DateField(null=True, blank=True)
    maximum_uses = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Order(models.Model):
    #     client = models.ForeignKey(ClientMembership, on_delete=models.SET_NULL, null=True, blank=True)
    #     payment_method = models.ForeignKey(PaymentMethod,on_delete=models.SET_NULL, null=True, blank=True)
    #     coupon_id = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    #     tax = models.FloatField(null=True, blank=True)
    #     total = models.FloatField()
    #     created_at = models.DateTimeField(auto_now_add=True)
    #     updated_at = models.DateTimeField(auto_now=True)
