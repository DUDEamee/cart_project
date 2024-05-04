from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("",views.index,name='home'),
    path("product_list",views.list_products,name='list_products'),
    path("product_details",views.detail_products,name='detail_products'),

]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)