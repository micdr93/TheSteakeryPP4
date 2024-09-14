from django import forms
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(
        queryset=Table.objects.all(),
        label="Table Selection",
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Select an available table"
    )
    
    class Meta:
        model = Booking
        fields = ['date', 'time', 'num_guests', 'special_requests', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'num_guests': forms.NumberInput(attrs={'min': 1}),
            'special_requests': forms.Textarea(attrs={'rows': 3}),
        }
        