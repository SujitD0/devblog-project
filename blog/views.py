from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import ContactForm
from django.http import JsonResponse


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print("CONTACT FORM SUBMISSION:")
            print(f"NAME: {name}, EMAIL: {email}, MESSAGE: {message}")
            return redirect('contact_success')
    else:  # ✅ handles GET requests
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form}) # ✅ always return

def contact_success(request):
    return render(request, 'contact_success.html')

def post_list(request):
    all_posts = Post.objects.all()
    context = {'all_the_posts': all_posts}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

#api function
def post_list_api(request):
    all_posts = Post.objects.all()
    context = {'all_the_posts': all_posts}
    data = {
        "posts":
            list(all_posts.values(
                'pk',
                'title',
                'content',
                'author',
                'created_at'
            ))
    }
    return JsonResponse(data)

def post_detail_api(request, pk):
    post = get_object_or_404(Post, pk=pk)

    data = {
        "post":{
            "pk": pk,
            "title": post.title,
            "content": post.content,
        }
    }
    return JsonResponse(data)