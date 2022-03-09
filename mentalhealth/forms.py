from django import forms
from .models import Entry, CheckIn


class EntryForm(forms.ModelForm):
    title = forms.CharField(required=True, label="Entry Title", widget=forms.Textarea(attrs={
        'class': "form-control rounded-0",
        'rows': "1",
        'placeholder': "Example Title"
    }))
    text = forms.CharField(required=True, label="Entry Text", widget=forms.Textarea(attrs={
        'class': "form-control rounded-0",
        'rows': "20",
        'placeholder': "Jot down whatever's on your mind, and when you're done don't forget to save your entry"
    }))

    class Meta:
        model = Entry
        fields = ['title', 'text']


