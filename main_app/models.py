from django.db import models
from django.contrib.auth.models import User

class QuranVerse(models.Model):
    arabic_text = models.TextField()
    urdu_translation = models.TextField()
    english_translation = models.TextField()
    word_by_word_translation = models.TextField(null=True, blank=True)

class Prayer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Sunnah(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    title_ar = models.CharField(max_length=100, blank=True, null=True)
    description_ur = models.TextField(blank=True, null=True)


class Alarm(models.Model):
    prayer_name = models.CharField(max_length=100)
    alarm_time = models.TimeField()
    location = models.CharField(max_length=255, null=True, blank=True)
    silent_mode = models.BooleanField(default=False)

class IslamicCalendarEvent(models.Model):
    month_name = models.CharField(max_length=100)  
    day_of_month = models.IntegerField()  
    event_name = models.CharField(max_length=255) 
    event_date = models.DateField()  
    description = models.TextField(null=True, blank=True) 

    def __str__(self):
        return f"{self.event_name} on {self.event_date}"

class Name(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Haddess(models.Model):
    title_ur = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100, blank=True, null=True)
    description_ur = models.TextField(blank=True, null=True)

class Setting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dark_mode = models.BooleanField(default=False)
    prayer_notification = models.BooleanField(default=True)
    alarm_time_slot = models.TimeField(null=True, blank=True)
    timezone = models.CharField(max_length=100, default='UTC')  # Timezone support
    location = models.CharField(max_length=255, null=True, blank=True)  # User's location
    
    def __str__(self):
        return f"Settings for {self.user.username}"
