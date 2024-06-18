from django import forms
from .models import NnaFAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = NnaFAQ
        fields = ['question', 'answer','category']