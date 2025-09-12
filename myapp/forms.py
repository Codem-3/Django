from django import forms

SHIFT_CHOICES = [
    ("morning", "Morning"),
    ("afternoon", "Afternoon"),
    ("evening", "Evening"),
]


class InputForm(forms.Form):
    first_name = forms.CharField(
        max_length=200,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your first name"}),
    )
    last_name = forms.CharField(
        max_length=200,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your last name"}),
    )
    email = forms.EmailField(
        max_length=200,
        label="Email Address",
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"}),
    )
    shift = forms.ChoiceField(choices=SHIFT_CHOICES, label="Preferred Shift")
    time_log = forms.DateTimeField(
        label="Date and Time",
        widget=forms.DateTimeInput(attrs={"placeholder": "YYYY-MM-DD HH:MM:SS"}),
    )
    feedback = forms.CharField(
        label="Feedback",
        widget=forms.Textarea(
            attrs={"rows": 4, "placeholder": "Enter your feedback here..."}
        ),
    )
