from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os.path

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about")
]  
# + static(settings.MEDIA_URL, document_root=os.path.join(os.path.join(os.path.dirname(__file__),"media").replace("\\","/")))
