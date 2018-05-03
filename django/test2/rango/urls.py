from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os.path

app_name = "rango"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("category/<slug:category_name_slug>",
         views.show_category, name="show_category"),
    # path("register/", views.register, name="register"),
    # path("login/", views.user_login, name="login"),
    # path("logout/", views.user_logout, name="logout"),
    # path("needlogin/", views.needlogin, name="needlogin"),
    path("add_category/", views.add_category, name="add_category"),
    path("goto/",views.goto,name="goto"),
    path("profile/<str:username>",views.profile,name="profile"),
    path("searchcategory/",views.searchcategory,name="searchcategory"),
    path("add_profile/<str:username>",views.register_profile,name="register_profile"),
    path("add_page/<slug:category_name_slug>", views.add_page, name="add_page"),
    path("profiles/",views.list_profiles,name="list_profiles"),
    path("like/",views.like_category,name="like_category"),
    path("suggest/",views.suggest_category,name="suggest_category")
]
# + static(settings.MEDIA_URL, document_root=os.path.join(os.path.join(os.path.dirname(__file__),"media").replace("\\","/")))
