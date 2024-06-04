from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Doctorinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    image_link = models.URLField(max_length=200, null=True, blank=True)
    specialty = models.CharField(max_length=100)
    availability = models.TextField() 


class Consultation(models.Model):
    patient = models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name='doctor', on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    notes = models.TextField()



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(null=True, blank=True)  # in centimeters
    weight = models.FloatField(null=True, blank=True)  # in kilograms
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')), null=True, blank=True)
    def bmi(self):
        if self.height and self.weight:
            return self.weight / ((self.height / 100) ** 2)
        return None

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

models.signals.post_save.connect(create_user_profile, sender=User)


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class HealthFact(models.Model):
    PLAN_TYPES = (
        ('nutrition', 'Nutrition'),
        ('exercise', 'Exercise'),
    )
    title = models.CharField(max_length=255)
    plan_type = models.CharField(max_length=100, choices=PLAN_TYPES)
    description = models.TextField()
    image_link = models.URLField(max_length=200, null=True, blank=True)