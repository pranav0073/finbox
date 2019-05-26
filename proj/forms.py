from django import forms

class NameForm(forms.Form):
    search_query = forms.CharField(label='Search Query', max_length=100)