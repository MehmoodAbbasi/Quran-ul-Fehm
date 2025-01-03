from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('quran-verses/', views.QuranVersesView.as_view(), name='quran_verses'),
    path('prayers/', views.PrayersView.as_view(), name='prayers'),
    path('sunnahs/', views.SunnahsView.as_view(), name='sunnahs'),
    path('alarms/', views.AlarmsView.as_view(), name='alarms'),
    path('islamic-calendar/', views.IslamicCalendarView.as_view(), name='islamic_calendar'),
    path('names/', views.NamesView.as_view(), name='names'),
    path('haddess/', views.HaddessView.as_view(), name='haddess'),
    path('settings/', views.SettingsUpdateView.as_view(), name='update_settings'),
    
    # Register and authentication URLs
    path('register/', views.RegisterView.as_view(), name='register'),
]
