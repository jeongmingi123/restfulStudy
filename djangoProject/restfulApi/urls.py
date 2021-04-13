from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from quickstart import views as quickView
from blog.views import Blog_list
from blog.views import BlogDetail, New_blog, Remove_blog, Edit_blog
from todo.views import TodoFormCreate, TodoListView, TodoDeleteView, TodoCreateView

router = routers.DefaultRouter()
router.register(r'users', quickView.UserViewSet)
router.register(r'groups', quickView.GroupViewSet)
router.register(r'post', quickView.PostViewSet)
# router.register(r'todo', )

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('blog_list/', Blog_list.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetail.as_view()),
    path('blog/new_blog', New_blog.as_view(), name="new_blog"),
    path('blog/<int:pk>/remove/', Remove_blog.as_view()),
    path('blog/<int:pk>/edit/', Edit_blog.as_view()),

    path('todo/todo_form/', TodoFormCreate.as_view(), name='todo_form'),
    path('todo/todo_list/', TodoListView.as_view(), name='todo_list'),
    path('todo/todo_create/', TodoCreateView.as_view(), name="todo_create"),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view()),

    # path('todo/todo_list/', createForm),

]
