
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^customer/', include('apps.clients.urls')),
    re_path(r'^manufacturer/', include('apps.manufacturer.urls')),
    re_path(r'^product/', include('apps.product.urls')),
    re_path(r'^order/', include('apps.order.urls')),
    re_path(r'^orderitem/', include('apps.orderitem.urls'))
]
