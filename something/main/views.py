from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from .forms import PostForm
from .models import Post


def main_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'main/main.html', context=context)


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'main/create_post.html'

    def post(self, request, *args, **kwargs):
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()
        else:
            return HttpResponse("Error")
        return redirect('main')
