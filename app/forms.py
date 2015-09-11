from django import forms
from app.models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())

    content = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'Please enter the content of the article'}))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Article

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
