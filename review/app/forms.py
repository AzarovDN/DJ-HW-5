from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise forms.ValidationError('Отзыв не может быть меньше 10 символов')
        return text

    class Meta(object):
        model = Review
        exclude = ('id', 'product')
        # initial = {'product': 1, }

