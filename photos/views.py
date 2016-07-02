from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse
from django.http import Http404

from .models import Photo

class PhotoCreate(CreateView):
    model = Photo
    fields = ('image', 'desc',)
    template_name = 'create_photo.html'

    def form_valid(self, form):
        new_photo = form.save(commit=False)
        new_photo.user = self.request.user
        new_photo.save()
        return super(PhotoCreate, self).form_valid(form)


def PhotoDelete(request, pk):
    photo = Photo.objects.get(pk=pk)

    if photo.user == request.user:
        photo.delete()
        return redirect('photos:list_photos')
    else:
        raise Http404("사용자가 일치하지 않습니다.")


class PhotoList(ListView):
    model = Photo
    template_name = 'photo_list.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoList, self).get_context_data(**kwargs)
        return context

class PhotoView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        return context

