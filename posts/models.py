from django.db import models as m

from accounts.models import Profile


def tweet_image_store(instance, filename):
    return f'profile/{instance.profile.user.username}/{instance.created_at}/{filename}'


class Tweet(m.Model):
    text = m.CharField(max_length=140)
    image = m.ImageField(
        upload_to=tweet_image_store, null=True, blank=True
    )
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)
    profile = m.ForeignKey(Profile, on_delete=m.PROTECT)

    def __str__(self):
        return self.text


class Reply(m.Model):
    tweet = m.ForeignKey(Tweet, on_delete=m.CASCADE)
    text = m.CharField(max_length=140)
    created_at = m.DateTimeField(auto_now_add=True)
    updated_at = m.DateTimeField(auto_now=True)
    profile = m.ForeignKey(Profile, on_delete=m.PROTECT)

    def __str__(self):
        return self.text
