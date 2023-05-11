from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from . import permissions as perm
from . import models
from . import serializers


class TweetViewSet(viewsets.ModelViewSet):
    queryset = models.Tweet.objects.all()
    serializer_class = serializers.TweetSerializer
    permission_classes = [perm.IsAuthorOrIsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    # @action(methods=['GET'],detail=False, url_path='reaction_url')
    # def reaction(self, request, pk=None):
    #     return Response({'key': 'value'})

    @action(methods=['POST'], detail=True,
            serializer_class=serializers.ReactionSerializer,
            permission_classes=[permissions.IsAuthenticated],
            )
    def reaction(self, request, pk=None):
        serializer = serializers.ReactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=self.request.user.profile, tweet=self.get_object())
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ReactionTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ReactionType.objects.all()
    serializer_class = serializers.ReactionTypeSerializer
    permission_classes = [perm.IsAdminOrReadOnly]


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = models.Reply.objects.all()
    serializer_class = serializers.ReplySerializer
    permission_classes = [perm.IsAuthorOrIsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])

    def perform_create(self, serializer):
        tweet_id = self.kwargs['tweet_id']
        tweet = models.Tweet.objects.get(id=tweet_id)
        serializer.save(tweet=tweet)


class ReplyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Reply.objects.all()
    serializer_class = serializers.ReplySerializer
    permission_classes = [permissions.IsAuthenticated, perm.IsAuthorOrIsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])


class ReplyListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Reply.objects.all()
    serializer_class = serializers.ReplySerializer
    permission_classes = [permissions.IsAuthenticated, perm.IsAuthorOrIsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(tweet_id=self.kwargs['tweet_id'])

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile, tweet_id=self.kwargs['tweet_id'])


# class ReactionCreateAPIView(generics.CreateAPIView):
#     queryset = Reaction.objects.all()
#     serializer_class = ReactionSerializer
#     authentication_classes = [TokenAuthentication, BasicAuthentication, SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(profile=self.request.user.profile, tweet_id=self.kwargs['tweet_id'])


class ReplyReactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.ReplyReaction.objects.all()
    serializer_class = serializers.ReplyReactionSerializer
    permission_classes = [perm.IsAuthorOrIsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            tweet_id=self.kwargs['tweet_id'],
            reply_id=self.kwargs['reply_id'],
            profile=self.request.user.profile
        )
