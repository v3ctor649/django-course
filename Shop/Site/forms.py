from django import forms

class Item(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput())