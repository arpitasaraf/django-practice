from django import forms

class TodoForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)