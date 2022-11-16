from .models import Fileupload
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .forms import FileUploadForm

# Create your views here.
# blog list up
# def index(request):
#     # 필요한 코드 넣기
#     posts=Post.objects.all().order_by('-pk')
#     # render(request, '템플릿파일',{'키': 변수 값})
#     return render(request, 'blog/index.html',{'posts':posts,})

def fileUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        img = request.FILES["imgfile"]
        fileupload = Fileupload(
            title=title,
            imgfile=img,
        )
        
        fileupload.save()
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'blog/fileupload.html', context)





# 하나의 post 상세페이지
#def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)
#
#    return render(request, 'blog/single_post_page.html',{'post':post,})