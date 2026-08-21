from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    post = Post.objects.all().order_by('id')
    paginator = Paginator(post , 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj' : page_obj})
