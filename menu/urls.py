from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name = 'menu'
urlpatterns = [
    path('', views.index, name='index' ),
    path('order/', views.order, name='order' ),
    path('order/(?P<pk>d+)/', views.order, name='order_with_pk' ),
    path('menu/', views.menu, name='menu' ),
    path('menu_mod/', views.menu_modify, name='menumod' ),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)