
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage,InvalidPage
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
import io,os
from django.http import StreamingHttpResponse


def homepage(request):
    return render(request, 'index.html')

def pptpage(request):
    return render(request, 'ppt.html')

def problemlist(request):

    return render(request, 'problemlist.html')

def send_zipfile(request):
    # 判断下载文件是否存在
    if not os.path.isfile(r'/home/ubuntu/django/Hostojgrade/ke.rar'):
        return HttpResponse("Sorry but Not Found the File1")

    def file_iterator(file_path, chunk_size=2048):
        """
        文件生成器,防止文件过大，导致内存溢出
        :param file_path: 文件绝对路径
        :param chunk_size: 块大小
        :return: 生成器
        """
        with open(file_path, mode='rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    try:
        # 设置响应头
        # StreamingHttpResponse将文件内容进行流式传输，数据量大可以用这个方法（.pdf,.mp3,.mp4等等什么样格式的文件都可以下载）
        response = StreamingHttpResponse(file_iterator(r'/home/ubuntu/django/Hostojgrade/ke.rar'))
        print(123)
        # 以流的形式下载文件,这样可以实现任意格式的文件下载
        response['Content-Type'] = 'application/octet-stream'
        print(123)
        # Content-Disposition就是当用户想把请求所得的内容存为一个文件的时候提供一个默认的文件名
        response['Content-Disposition'] = 'attachment;filename={file_name}{format}'.format(
            file_name='my_rar', format=".rar")
    except:
        return HttpResponse("Sorry but Not Found the File12")

    # 在这里千万记得return,否则不会出现下载
    return response



