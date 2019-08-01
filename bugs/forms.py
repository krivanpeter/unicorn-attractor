from django import forms
from .models import Bug, BugImages
import re


class BugReportForm(forms.ModelForm):
    # Bug Report Form
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control bug-input',
            'placeholder': 'Describe the issue...',
            'rows': '3'}),
        label='The issue')

    class Meta:
        model = Bug
        fields = (
            'title',
            'content',
        )

    def clean_title(self):
        title = re.sub(' +', ' ', self.cleaned_data.get('title').strip())
        return title

    def clean_content(self):
        content = re.sub(' +', ' ', self.cleaned_data.get('content').strip())
        return content

class BugImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = BugImages
        fields = (
            'image',
        )