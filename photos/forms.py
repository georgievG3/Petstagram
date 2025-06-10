from django import forms

from photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCreateForm(PhotoBaseForm):
    ...


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ['photo']


