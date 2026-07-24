from . import views 
from django.urls import path , re_path

urlpatterns = [
    path('post/<int:post_id>', views.post_details , name="post-details"),
    path('users/<str:username>' , views.users, name='username'),
    path('article/<int:year>/<int:month>/<int:days>', views.article_details , name='article_details'),

    re_path(r'^article/(?P<year>[0-9]{4})/$',views.article_by_year , name='article_by_year'),   
]
