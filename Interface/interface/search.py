from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        ctx['rltt'] = request.POST['qq']
        ctx['num'] = 3
    return render(request, "post.html", ctx)