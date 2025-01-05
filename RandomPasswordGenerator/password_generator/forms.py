from django import forms
class Password(forms.Form):
    length=forms.IntegerField(label='Enter the Password Length',min_value=1,max_value=100, required=True)
    uppercase=forms.BooleanField(required=False,label='uppercase')
    lowercase=forms.BooleanField(required=False,label='lowercase')
    digits=forms.BooleanField(required=False,label='digits')
    punctuation=forms.BooleanField(required=False,label='punctuation')