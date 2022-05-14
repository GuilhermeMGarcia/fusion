from django.urls import path
from .views import IndexView

from fusion import settings
from django.contrib.auth import views as auth_views

app_name = 'fusion_core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
