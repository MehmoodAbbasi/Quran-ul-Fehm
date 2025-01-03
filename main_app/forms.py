# islamic_app/forms.py

from django import forms
from .models import QuranVerse, Prayer, Sunnah, Alarm, IslamicCalendarEvent, Name, Setting, Haddess

class QuranVerseForm(forms.ModelForm):
    class Meta:
        model = QuranVerse
        fields = ['arabic_text', 'urdu_translation', 'english_translation', 'word_by_word_translation']

class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ['name', 'description']

class SunnahForm(forms.ModelForm):
    class Meta:
        model = Sunnah
        fields = ['title', 'description', 'title_ar', 'description_ur']

class HaddessForm(forms.ModelForm):
    class Meta:
        model = Haddess
        fields = ['title_ur', 'title_ar', 'description_ur']


class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = ['prayer_name', 'alarm_time', 'location', 'silent_mode']

class IslamicCalendarEventForm(forms.ModelForm):
    class Meta:
        model = IslamicCalendarEvent
        fields = ['event_name', 'event_date']

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ['name', 'description']

class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = ['dark_mode', 'prayer_notification', 'alarm_time_slot', 'timezone', 'location']
        widgets = {
            'alarm_time_slot': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'timezone': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your location'}),
        }

    def clean_alarm_time_slot(self):
        alarm_time = self.cleaned_data['alarm_time_slot']
        if alarm_time and alarm_time < "06:00":
            raise forms.ValidationError("The alarm time must be after 6 AM.")
        return alarm_time