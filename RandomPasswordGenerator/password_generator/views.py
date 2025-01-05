from django.shortcuts import render
from .forms import Password
import string
import random

def password_generator(request):
    generated_password=None
    form=Password(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            length=form.cleaned_data['length']
            uppercase=form.cleaned_data.get('uppercase', False)
            lowercase=form.cleaned_data.get('lowercase', False)
            digits=form.cleaned_data.get('digits', False)
            punctuation=form.cleaned_data.get('punctuation', False)
            characterList = ''
            if uppercase:
                characterList+=string.ascii_uppercase
            if lowercase:
                characterList+=string.ascii_lowercase
            if digits:
                characterList+=string.digits
            if punctuation:
                characterList+=string.punctuation
            if characterList:
                generated_password=''.join(random.choice(characterList) for _ in range(length))
            else:
                generated_password="No character set selected"
        else:
            generated_password="Please correct the errors in the form"
    return render(request, 'password_generator.html',{'form': form,'generated_password': generated_password})
