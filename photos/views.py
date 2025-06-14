from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from common.forms import CommentForm
from photos.forms import PhotoCreateForm, PhotoEditForm
from photos.models import Photo


# Create your views here.
def photo_add_view(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, 'photos/photo-add-page.html', context)


def photo_details_view(request, pk:int):
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.all
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'photos/photo-details-page.html', context)


def photo_edit_view(request, pk:int):
    photo = Photo.objects.get(pk=pk)
    form = PhotoEditForm(request.POST or None, instance=photo)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        'photo': photo,
        'form': form,
    }

    return render(request, 'photos/photo-edit-page.html', context)

def photo_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')



