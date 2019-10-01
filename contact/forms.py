from django import forms
from .models import Message

class ContactForm(forms.Form):
    email = forms.EmailField(
        label=False,
        widget=forms.TextInput(attrs={'placeholder': 'Email.', 'type': 'email'}))
    message = forms.CharField(
        label=False,
        widget=forms.Textarea(attrs={'placeholder': 'Message.'}))

    def process(self):
        clean_data = self.cleaned_data
        email = clean_data["email"]
        message = clean_data["message"]

        Message.objects.create(email=email, message=message)