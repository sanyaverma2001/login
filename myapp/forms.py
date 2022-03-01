from django.forms import ModelForm,fields, models
from . models import user_register


class userform(ModelForm):
    class Meta:
        model=user_register
        fields=['username','email','password']
