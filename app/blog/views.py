from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.

from .forms import PostModelForm
from .models import PostModel


def show_leshes(request):

    template_path = 'six.html'

    return render(request, template_path)


def post_model_create_view(request):

    form = PostModelForm(request.POST or None)

    if form.is_valid():

        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'The blog post was created!')

        return HttpResponseRedirect('/blog/{num}'.format(num=obj.id))

    context_dictionary = {
        'form': form
    }

    template_path = 'create_page.html'

    return render(request, template_path, context_dictionary)


def post_model_detail_view(request, id=None):

    qs = get_object_or_404(PostModel, id=id)
    template_path = 'detail_page.html'

    context_dictionary = {
        'object': qs,
    }

    return render(request, template_path, context_dictionary)


def post_model_list_view(request):

    qs = PostModel.objects.all()
    template_path = 'new_page.html'

    context_dictionary = {
        'objected_list': qs,
    }

    print(qs)

    return render(request, template_path, context_dictionary)


@login_required()
def login_required_view(request):

    qs = PostModel.objects.all()

    context_dictionary = {
        'objected_list': qs,
    }

    if request.user.is_authenticated:
        template_path = 'new_page.html'
    else:
        raise Http404

    return render(request, template_path, context_dictionary)
