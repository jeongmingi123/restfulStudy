from django.urls import path
from . import views


# /blog/
app_name = 'blog'
urlpatterns = [

    # FBV
    # path('', MyView.as_view(), name='index'),
    # path('post_detail/<int:post_id>', views.PostDetail.as_view, name='post_detail'),
    # path('post_get/', views.post_get),
    # path('post_create/', views.post_create, name='create'),
    # path('post_delete/', views.post_delete),

    # CBV
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('post_detail/<int:post_id>', views.PostDetail.as_view(), name='post_detail'),
    path('post_create/', views.PostCreate.as_view(), name='post_create'),
    path('post_update/<int:post_id>', views.PostUpdate.as_view(), name='post_update'),
    path('post_update/', views.PostUpdate.as_view(), name='post_update'),
    path('post_delete/<int:post_id>', views.PostDelete.as_view()),
]
