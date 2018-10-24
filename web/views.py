from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    # post_list = list()
    # for count, post in enumerate(posts):
    #     post_list.append("no.{}:".format(str(count)) + str(post) + "<hr>")
    #     post_list.append("<small>" + str(post.body) + "</small><br><br>")
    # return HttpResponse(post_list)
    now = datetime.now()
    return render(request, "heatmap.html", locals())


def showpost(request,slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, "post.html", locals())
    except:
        return redirect('/')
def echarts(request):
    return render(request, 'echarts.html')

def heatmap(request):
    return render(request, 'heatmap.html')

# def index(request):
#     #return HttpResponse('Hello!')
#     if request.method == "POST":
#         un = request.POST.get("un", None)
#         pw = request.POST.get("pw", None)
#         print(un, pw)
#     return render(request, "index.html")


