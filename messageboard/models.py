from django.db import models

# Create your models here.


class Post(models.Model):
    """Our core thing - a single message."""
    
    sent = models.DateTimeField(
        null=False,
        auto_now_add=True,
        help_text="The time when this post was created."
    )
    title = models.CharField(
        max_length=500,
        null=True,
        help_text="The post's title."
    )
    content = models.TextField(
        null=False,
        help_text="The post's content."
    )
