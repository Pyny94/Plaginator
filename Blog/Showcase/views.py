from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render
from django.core.paginator import Paginator
from Showcase.models import Post

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request,'Showcase/index.html',{'page_obj':page_obj})