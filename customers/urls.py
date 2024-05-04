from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("account/",views.show_account,name='account'),

]
urlpatterns +=static(settings.MEDIA_URL,document_roof=settings.MEDIA_ROOT)