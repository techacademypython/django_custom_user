from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=255)

    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    def get_likers(self):
        return [like.user for like in self.like_set.all()]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.IntegerField(choices=(
        (0, "Like"),
        (1, "Unlike")
    ),
        default=0
    )

    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"