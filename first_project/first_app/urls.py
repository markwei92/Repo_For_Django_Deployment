from django.urls import path
from first_app import views
from first_app.views import user_login

# Template Tagging
app_name = 'first_app'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.users, name='users'),
    path('relative/', views.relative,name='relative'),
    path('other/', views.other,name='other'),
    path('register', views.register,name='register'),
    path('user_login', views.user_login,name='user_login'),
]

