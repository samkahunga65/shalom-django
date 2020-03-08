from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name = 'management'
urlpatterns = [
    path('', views.shalom_info, name='shalominfo' ),
    path('menu', views.menu_modify, name='menumod' ),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)