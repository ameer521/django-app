from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from form1.models import Post
from django.contrib import messages
from .forms import Postform
# Create your views here.

@login_required()   # login_url defined in settings. so not need to set here, same for all functions
def home(request):
    #print(dir(request))  # to see all functions in request
    #print(request.method)  # for method of request (post or get)
    #print(request.get_full_path())  #for getting the url or path of the request.
    return HttpResponse("Homepage")


@login_required(login_url='/admin')
def test(request):
    response = HttpResponse(content_type='text/html')  # for content type setting
    response.write("test1")
    response.write("test2")
    response.content = 'hello'   #  like returm HttpRespone
    return response

############################################################################

@login_required(login_url='/admin')
def redirect(request):
    return HttpResponseRedirect("https://www.google.com")             # for redirection


###############################################################################



@login_required(login_url='/admin')
def showing(request):
    post = Post.objects.all()
    username = request.user
    print(username)
    if request.user.is_authenticated:    # for checking logged in or not
        print("logged in ")
        return render(request, "form1/homepage.html", {"post": post, "username": username})
    else:
        raise Http404   # for showing 404 error instead of error(template does not exist or value error or other)


#################################################################################

def detail_view(request):    # for fetching models by " get " condition
    post = Post.objects.get(id=1)
    return HttpResponse(post.author)

#################################################################################

def detail_view2(request, id = None):
    post = get_object_or_404(Post,id=id)   # if , no objects found , then it will show the 404 instead of errors.
    return HttpResponse(post.title)


########################################################################


def  createview(request):
    #if request.method == "POST":
        #print(request.POST)
        #form = Postform(request.POST)
        #if form.is_valid():
         #   form.save(commit=False)
          #  print(form.cleaned_data)


    form = Postform(request.POST or None)   # Here, The request checked whether " POST " or not. if it " POST ".
    if form.is_valid():  # form validation done here,
        obj = form.save(commit=False)   # we  can't directly save the content as form.save , So , we sets form.save to object (variable)
        obj.save()  # then saves it
        messages.success(request,"Created")
        #return HttpResponse("Success")


    return render(request,'form1/createview.html',{"form":form})


#####################################################################


def update_view(request,id=None):
    obj = get_object_or_404(Postform,id=id)
    form = Postform(request.POST or None, instance=id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()

    return render(request,'form1/createview.html',{"form":form})



