from django.contrib import admin
from django.urls import path

from app.views import BlogListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogListView.as_view(), name='index'),
    # path('', index, name='index'),

]
