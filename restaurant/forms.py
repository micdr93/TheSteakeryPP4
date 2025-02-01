from django import forms
from .models import Booking, Table, SpecialRequest

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(
        queryset=Table.objects.all(),
        label="Table Selection",
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Select an available table",
    )
    special_requests = forms.ModelMultipleChoiceField(
        queryset=SpecialRequest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Special Requests"
    )
    
    class Meta:
        model = Booking
        fields = [
            'date', 'start_time', 'num_guests', 
            'special_requests', 'table'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'num_guests': forms.NumberInput(attrs={'min': 1}),
        }