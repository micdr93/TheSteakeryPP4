from django import forms
from datetime import time, timedelta, datetime, date

class TwoHourIntervalTimeWidget(forms.Select):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = self.generate_time_choices()

    def generate_time_choices(self):
        choices = []
        current_time = time(12, 0)
        closing_time = time(23, 0) 
        while current_time < closing_time:
            choices.append((
                current_time.strftime('%H:%M'), current_time.strftime('%I:%M %p')
            ))
            current_time = (datetime.combine(date.today(), current_time) + timedelta(hours=2)).time()
        return choices