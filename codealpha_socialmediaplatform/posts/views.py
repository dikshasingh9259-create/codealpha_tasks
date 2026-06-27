from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Like,Comment
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from accounts.models import Profile

@login_required
def home_view(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    
    # Safely get or create profile if it doesn't exist yet
    Profile.objects.get_or_create(user=profile_user)
    
    posts = profile_user.posts.all()
    context = {
        'profile_user': profile_user,
        'posts': posts,
        'post_count': posts.count()
    }
    return render(request, 'profile.html', context)  

@login_required
def like_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like_filter = Like.objects.filter(user=request.user, post=post)
    
    if like_filter.exists():
        like_filter.delete() # Unlike if already liked
    else:
        Like.objects.create(user=request.user, post=post)
        
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def add_comment_view(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        comment_text = request.POST.get('comment_text', '').strip()
        if comment_text:
            Comment.objects.create(user=request.user, post=post, text=comment_text)
    return redirect(request.META.get('HTTP_REFERER', 'home'))



def search_users_view(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        # Searches for usernames that contain the search text
        results = User.objects.filter(Q(username__icontains=query)).exclude(id=request.user.id)
    return render(request, 'search_results.html', {'results': results, 'query': query})