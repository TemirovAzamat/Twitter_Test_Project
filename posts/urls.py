from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TweetViewSetAPIView, ReplyViewSetAPIView

router = DefaultRouter()
router.register('tweets', TweetViewSetAPIView)
router.register('replies', ReplyViewSetAPIView)


urlpatterns = [
    # path('viewset/tweets/', TweetViewSetAPIView.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/tweets/<int:pk>/', TweetViewSetAPIView.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    #
    # path('viewset/posts/', ReplyViewSetAPIView.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/posts/<int:pk>/', ReplyViewSetAPIView.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    path('viewset/', include(router.urls))
]
