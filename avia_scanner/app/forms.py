from django import forms
from .widgets import AjaxInputWidget
from .models import City

class SearchTicket(forms.Form):

    from_town = forms.CharField(label='Город отправления',
                                widget=AjaxInputWidget(attrs={'class': 'inline right-margin'},
                                                       url='api/city_ajax'))
    to_town = forms.ModelChoiceField(label='Город прибытия',
                                     queryset=City.objects.all().order_by('name'))
    date = forms.DateField(label='Дата',
                           widget=forms.TextInput(attrs={'class': 'datepicker'}))









