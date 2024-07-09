from django.db import models


class Links(models.Model):
    """Links to accounts"""
    link = models.URLField()

    def __str__(self):
        return self.link


class AccountDetail(models.Model):
    """Account social details"""
    objects = models.Manager
    url = models.URLField()

    post_count = models.PositiveIntegerField(default=0)
    media_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f'User: {self.url}, \n post_count: {self.post_count}, \n'
            f'media_count: {self.media_count}, \n likes_count: {self.likes_count}'
            f'\n last_updated: {self.last_updated}'
            )
