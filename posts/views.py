
from django.shortcuts import redirect, render

# Create your views here.
from .models import Post, Profile
from .forms  import NewPostForm


def post_list(request):
    posts = Post.objects.all()

    post_name = request.GET.get('post_name')
    if post_name != '' and post_name is not None:
        posts = posts.filter(title__icontains=post_name)

    return render(request , 'posts/post_list.html' , {
        'posts': posts,
       
    })



def post_create(request):
    if request.method == 'POST':
        form = NewPostForm(data=request.POST , files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            obj = form.instance
            alert = True
            return render(request , 'posts/post_create.html',  {
                'obj': obj , 
                'alert': alert
            })
    else:
        form = NewPostForm()
        return render(request , 'posts/post_create.html', {'form': form})
