from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView
from blog.models import Post


class PostDetailView(DetailView):
    model = Post


def news(request):
    posts = Post.objects.all()
    return render_to_response('blog/news.html', {'object_list': posts},
                              context_instance=RequestContext(request))