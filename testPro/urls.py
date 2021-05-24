from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from store.views import auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),

    url('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
]


