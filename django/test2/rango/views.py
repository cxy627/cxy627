from django.shortcuts import render, reverse, redirect, HttpResponse, HttpResponseRedirect
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm
from .models import Category, Page, User, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
import urllib

def suggest_category(request):
    def get_category_list(max_results=0, contain=""):
        cat_list = []
        if contain:
            cat_list = Category.objects.filter(name__contains=contain)
        if max_results > 0:
            if len(cat_list) > max_results:
                cat_list = cat_list[:max_results]
        return cat_list
    cat_list = []
    contain = ''
    if request.method == 'GET':
        contian = request.GET["suggestion"]
        cat_list = get_category_list(8,contian)
    return render(request,"rango/cats.html",{"cats":cat_list})


@login_required
def like_category(request):
    cat_id = None
    if request.method == "GET":
        cat_id = request.GET['category_id']
        likes = 0
        if cat_id:
            cat = Category.objects.get(id=int(cat_id))
            if cat:
                likes = cat.likes + 1
                cat.likes = likes
                cat.save()
    return HttpResponse(likes)


def searchcategory(request):
    if request.method == "POST":
        searchtext = request.POST.get("searchtext", '')
        try:
            category = Category.objects.get(name=searchtext)
        except Category.DoesNotExist:
            return redirect(reverse("rango:index"))
        return redirect(reverse("rango:show_category", args=[category.slug]))


def index(request):
    request.session.set_test_cookie()
    Category_list = Category.objects.order_by("-likes")[:5]
    Page_list = Page.objects.order_by("-views")[:5]
    visitor_cookie_handler(request)
    context_dict = {"categories": Category_list,
                    "pages": Page_list, "visits": request.session["visits"]}
    return render(request, "rango/index.html", context=context_dict)


def about(request):
    try:
        if request.session.test_cookie_worked:
            print("cookie存在并工作")
            request.session.delete_test_cookie()
    except Exception:
        pass
    return render(request, "rango/about.html")


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category).order_by("-views")
        context_dict["pages"] = pages
        context_dict["category"] = category
    except Category.DoesNotExist:
        context_dict["pages"] = None
        context_dict["category"] = None

    context_dict['query'] = category.name
    result_list = []
    if request.method == "POST":
        query = request.POST["query"].strip()
        if query:
            # result_list = run_query(query)#没有合适的搜索API接口
            context_dict["query"] = query
            # context_dict["result_list"] = result_list
    return render(request, "rango/category.html", context=context_dict)


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'website':  userprofile.website,  'picture':  userprofile.picture})
    if request.method == "POST":
        form = UserProfileForm(
            request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('rango:profile',  user.username)
        else:
            print(form.errors)
    return render(request,  'rango/profile.html',
                  {'userprofile':  userprofile,  'selecteduser':  user,  'form':  form})


@login_required
def list_profiles(request):
    userprofile_list = UserProfile.objects.all()
    return render(request,  'rango/list_profiles.html',
                  {'userprofile_list':  userprofile_list})


@login_required
def register_profile(request, username):
    form = UserProfileForm()
    if request.method == "GET":
        context_dict = {"form": form, "username": username}
        return render(request, "rango/profile_registration.html", context_dict)
    else:
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = User.objects.get(username=username)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
        return redirect(reverse("rango:index"))


def goto(request):
    page_id = None
    if request.method == "GET":
        if "page_id" in request.GET:
            page_id = request.GET["page_id"]
    if page_id:
        try:
            page = Page.objects.get(id=page_id)
        except Page.DoesNotExist:
            return redirect(reverse("rango:index"))
        page.views += 1
        return redirect(page.url)
    else:
        return redirect(reverse("rango:index"))


@login_required
def add_category(request):

    form = CategoryForm()  # 新建一个表单

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat = form.save(commit=True)
            print("类别已添加: %s " % cat)
            return index(request)
        else:
            print(form.errors)
    return render(request, "rango/add_category.html", {"form": form})


@login_required
def add_page(request, category_name_slug):
    form = PageForm()
    context_dict = {"form": form}
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    if category and request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.category = category  # 把唯一没有填的外键填上
            cat.views = 0
            cat.save()
            print("页面已添加 %s" % cat)
            return index(request)
        else:
            print(form.errors)
    context_dict["category"] = category
    return render(request, "rango/add_page.html", context_dict)

# def register(request):
#     registered=False
#     if request.method=="POST":
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user=user_form.save(commit=True)
#             user.set_password(user.password)
#             user.save()

#             profile = profile_form.save(commit=False)
#             profile.user = user
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']

#             profile.save()

#             registered = True
#         else:
#             print(user_form.errors,profile_form.errors)
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#     return render(
#         request,
#         'rango/register.html',
#         {
#             'user_form':user_form,
#             'profile_form':profile_form,
#             'registered':registered
#         }
#         )

# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username",'')
#         password = request.POST.get("password",'')

#         user = authenticate(username=username,password=password)
#         if user:
#             if user.is_active:
#                 login(request,user)
    # return HttpResponseRedirect(reverse('rango:index'))
#             else:
#                 return HttpResponse("你的账号不能登陆")
#         else:
#             print('invalid login details:{0},{1}'.format(username,password))
#             return HttpResponse('登陆信息有误')
#     else:
#         return render(request,'rango/login.html')

# def needlogin(request):
#     return render(request,'rango/needlogin.html')

# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('rango:index'))


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, "visits", "1"))

    last_visit_cookie = get_server_side_cookie(
        request, "last_visit", str(datetime.now()))
    last_visit_time = datetime.strptime(
        last_visit_cookie[:-7], r'%Y-%m-%d  %H:%M:%S')
    if (datetime.now() - last_visit_time).seconds > 0:
        visits += 1
        request.session["last_visit"] = str(datetime.now())
    else:
        request.session["last_visit"] = last_visit_cookie

    request.session['visits'] = visits


def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

# Create a new class that redirects the user to the index page,
# if successful at logging
