from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Tweet, Reply
from .serializers import TweetSerializer, ReplySerializer
from .permissions import IsAuthorORIsAuthenticated


class TweetViewSetAPIView(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorORIsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class ReplyViewSetAPIView(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
