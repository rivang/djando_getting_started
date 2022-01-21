from datetime import date
from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput, TimeInput, TextInput
from .models import Meeting


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }

        def clean_date(self):
            d = self.cleaned_data_get("date")
            if d < date.today():
                raise ValidationError("Meeting cannot be in the past")
            return d
