from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsAuthorOrIsAuthenticated, IsAdminOrReadOnly
from .models import Reply, Tweet, Reaction, ReactionType
from .serializers import TweetSerializer, ReplySerializer, ReactionSerializer, ReactionTypeSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrIsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    # @action(methods=['GET'],detail=False, url_path='reaction_url')
    # def reaction(self, request, pk=None):
    #     return Response({'key': 'value'})

    @action(methods=['POST'], detail=True,
            serializer_class=ReactionSerializer,
            permission_classes=[permissions.IsAuthenticated],
            authentication_classes=[BasicAuthentication, SessionAuthentication, TokenAuthentication]
            )
    def reaction(self, request, pk=None):
        serializer = ReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=self.request.user.profile, tweet=self.get_object())
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ReactionTypeViewSet(viewsets.ModelViewSet):
    queryset = ReactionType.objects.all()
    serializer_class = ReactionTypeSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrIsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])

    def perform_create(self, serializer):
        tweet_id = self.kwargs['tweet_id']
        tweet = Tweet.objects.get(id=tweet_id)
        serializer.save(tweet=tweet)


class ReplyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrIsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])


class ReplyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrIsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter().filter(tweet_id=self.kwargs['tweet_id'])


# class ReactionCreateAPIView(generics.CreateAPIView):
#     queryset = Reaction.objects.all()
#     serializer_class = ReactionSerializer
#     authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(profile=self.request.user.profile, tweet_id=self.kwargs['tweet_id'])
