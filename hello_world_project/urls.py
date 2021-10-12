from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import helloworldfunction, HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw_h1_tag/', helloworldfunction),
    path('hw_index_html/', HelloWorldClass.as_view()),
    path('', include('helloworldapp.urls')),
]
