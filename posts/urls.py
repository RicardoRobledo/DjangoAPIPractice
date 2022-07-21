from django.urls import path
# from .views import UserList, UserDetail, PostList, PostDetail # new
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet

'''
urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
'''

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls