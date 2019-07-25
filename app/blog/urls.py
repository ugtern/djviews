from django.urls import path
from django.conf.urls import url

from .views import post_model_list_view, post_model_detail_view, post_model_create_view, show_leshes
urlpatterns = [
    path('', post_model_list_view, name='list'),
    url(r'^(?P<id>\d+)/$', post_model_detail_view, name='detail'),
    path('create/', post_model_create_view, name='create'),
    path('six/', show_leshes, name='show_leshes'),
    # path('admin/', admin.site.urls),
    # path('', home, name='home'),
    # path('redirect/', redirect_to_page, name='home'),
    # path('page/', home_page, name='home'),
]
