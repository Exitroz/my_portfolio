
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Tag, Donation
from .forms import BlogPostForm, CommentForm


def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    tags = Tag.objects.all()
    return render(request, 'index.html', {'posts': posts, 'tags': tags})

def post1(request):
    return render(request, 'blog-post-1.html')

def post2(request):
    return render(request, 'post-2.html')

def post3(request):
    return render(request, 'post-3.html')

def post4(request):
    return render(request, 'post-4.html')

def post5(request):
    return render(request, 'post-5.html')

def post6(request):
    return render(request, 'post-6.html')

def portfolio1(request):
    return render(request, 'portfolio-1.html')

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.filter(approved=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog-post-1.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })

def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form.save_m2m()  # Save the tags
            return redirect('blog_list')
    else:
        form = BlogPostForm()

    return render(request, 'blog/add_post.html', {'form': form})

def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = BlogPost.objects.filter(tags=tag)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag': tag})