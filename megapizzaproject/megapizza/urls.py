from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,  name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/', views.catalog, name='catalog'),
    path('corf/', views.corf, name='corf'),
    path('pers_cab/', views.pers_cab, name='pers_cab'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('new/', views.new, name='new'),
    path('', include('django.contrib.auth.urls'), name='login'),
    path('signup/', views.SignUp.as_view(), name="signup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)