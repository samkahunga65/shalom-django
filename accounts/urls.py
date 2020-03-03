from django.urls import path
from . import views
from menu import views as menu_views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup_view, name='signup' ),
    path('logout/', views.logout_view, name='logout' ),
    path('login/', views.login_view, name='login' ),
    path('home/', menu_views.index, name='home' ),

]
