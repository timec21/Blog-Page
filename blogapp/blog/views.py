from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Blogs

# Create your views here.
# view kullanıcının göreceği templatelerdir
# views.py dosyasının içindeki her bir fonskiyon gönderilen requeste göre belirtilen templatelere yönlendirir

def index(request):
    all_blogs = Blogs.objects.all()
    return render(request, "blog/index.html" ,{"blogs": all_blogs})

def blogs(request):
    all_blogs = Blogs.objects.all()
    return render(request, "blog/_blogs.html", {"blogs": all_blogs})

def blog_details(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/b_details.html', {'blog': blog})

def blog_list(request):
    blogs = Blogs.objects.all()
    paginator = Paginator(blogs, 10)  ,
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog_list.html', {'page_obj': page_obj})
