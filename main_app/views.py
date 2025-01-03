from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class QuranVersesView(View):
    def get(self, request):
        verses = QuranVerse.objects.all()
        return render(request, 'quran_verses.html', {'verses': verses})

    
class PrayersView(View):
    def get(self, request):
        prayers = Prayer.objects.all()
        return render(request, 'prayers.html', {'prayers': prayers})

class SunnahsView(View):
    def get(self, request):
        sunnahs = Sunnah.objects.all()
        return render(request, 'sunnahs.html', {'sunnahs': sunnahs})

class AlarmsView(View):
    def get(self, request):
        alarms = Alarm.objects.all()
        return render(request, 'alarms.html', {'alarms': alarms})
class HaddessView(View):
    def get(self, request):
        haddess = Haddess.objects.all()
        return render(request, 'haddess.html', {'haddess': haddess})

class IslamicCalendarView(View):
    def get(self, request):
        months = {}
        events = IslamicCalendarEvent.objects.all().order_by('event_date')
        for event in events:
            if event.month_name not in months:
                months[event.month_name] = []
            months[event.month_name].append(event)
        return render(request, 'islamic_calendar.html', {'months': months})

class NamesView(View):
    def get(self, request):
        alarms = Alarm.objects.all()
        return render(request, 'names.html', {'alarms': alarms})

class SettingsUpdateView(LoginRequiredMixin, View):
    """
    CBV to handle the user's settings update with advanced features.
    """
    def get(self, request):
        setting, created = Setting.objects.get_or_create(user=request.user)
        form = SettingForm(instance=setting)
        return render(request, 'settings.html', {'form': form, 'setting': setting})

    def post(self, request):
        setting, created = Setting.objects.get_or_create(user=request.user)
        form = SettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            messages.success(request, "Your settings have been updated successfully!")
            return redirect('update_settings')  # Redirect to the same page after saving
        return render(request, 'settings.html', {'form': form, 'setting': setting})

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
