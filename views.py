from django.shortcuts import render
from .models import Post

def post_list(request):
    # 글 목록을 가져오는 로직을 작성
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

def post_create(request):
    # 글 작성 폼을 보여주는 로직을 작성
    if request.method == 'POST':
        # 폼 데이터를 처리하는 로직을 작성
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post_create.html', context)

def post_detail(request, post_id):
    # 특정 글의 상세 정보를 가져오는 로직을 작성
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'post_detail.html', context)
