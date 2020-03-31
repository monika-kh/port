import re

from django import forms

from .models import Apply


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'job', 'resume']

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not re.match(r"^[a-zA-Z\s]+$", name):
            raise forms.ValidationError(
                "First Name Consists Of Only Alphabetical Characters"
            )
        return name
