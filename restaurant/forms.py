from django import forms
from .models import Booking, Table, SpecialRequest

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(
        queryset=Table.objects.all(),
        label="Table Selection",
        widget=forms.Select(attrs={'class': 'form-control form-center'}),
       
    )
    

    additional_requests = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-center', 'rows': 3}),
        required=False,
        label="Special Requests"
    )

    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'num_guests', 'additional_requests', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-center'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-center'}),
            'num_guests': forms.NumberInput(attrs={'min': 1, 'class': 'form-control form-center'}),
        }