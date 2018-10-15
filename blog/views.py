from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.order_by('-created_date') 
    #select * from Post order by created_date DESC;返回一个列表
    return render(request, 'blog/post_list.html', {'posts':posts})

def show(request,post_id):
	posts = get_object_or_404(Post,pk=post_id)
	#找到主键为post_id，找不到就返回404的页面
	return render(request, 'blog/post_detail.html', {'posts':posts})