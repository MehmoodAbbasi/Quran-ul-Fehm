from django.contrib import admin
from .models import QuranVerse, Prayer, Sunnah, Alarm, IslamicCalendarEvent, Name, Setting, Haddess

class QuranVerseAdmin(admin.ModelAdmin):
    list_display = ('arabic_text', 'urdu_translation', 'english_translation')
    search_fields = ('arabic_text', 'urdu_translation', 'english_translation')

class PrayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class SunnahAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'title_ar', 'description_ur')
    search_fields = ('title',)

class AlarmAdmin(admin.ModelAdmin):
    list_display = ('prayer_name', 'alarm_time', 'location', 'silent_mode')
    list_filter = ('silent_mode',)
    search_fields = ('prayer_name', 'location')

class IslamicCalendarEventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date')
    list_filter = ('event_date',)
    search_fields = ('event_name',)

class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


class HaddessAdmin(admin.ModelAdmin):
    list_display = ('title_ur', 'title_ar', 'description_ur')
    search_fields = ('title_ur', 'title_ar', 'description_ur')
    list_filter = ('title_ar',)
    
class SettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'dark_mode', 'prayer_notification', 'alarm_time_slot')
    list_filter = ('dark_mode', 'prayer_notification')
    search_fields = ('user__username',)

admin.site.register(QuranVerse, QuranVerseAdmin)
admin.site.register(Prayer, PrayerAdmin)
admin.site.register(Sunnah, SunnahAdmin)
admin.site.register(Alarm, AlarmAdmin)
admin.site.register(IslamicCalendarEvent, IslamicCalendarEventAdmin)
admin.site.register(Name, NameAdmin)
admin.register(Haddess, HaddessAdmin)

admin.site.register(Setting, SettingAdmin)
