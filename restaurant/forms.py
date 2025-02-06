from django import forms
from .models import Booking, Table, SpecialRequest

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(
        queryset=Table.objects.all(),
        label="Table Selection",
        widget=forms.Select(attrs={'class': 'form-control form-center'}),
        help_text="Select an available table",
    )
    special_requests = forms.ModelMultipleChoiceField(
        queryset=SpecialRequest.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        required=False,
        label="Special Requests"
    )
    additional_requests = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-center', 'rows': 3}),
        required=False,
        label="Additional Requests"
    )

    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'num_guests', 'special_requests', 'additional_requests', 'table']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-center'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-center'}),
            'num_guests': forms.NumberInput(attrs={'min': 1, 'class': 'form-control form-center'}),
        }