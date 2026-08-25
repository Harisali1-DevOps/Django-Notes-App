from django.db import models


class Note(models.Model):
    COLOR_CHOICES = [
        ("yellow", "Yellow"),
        ("blue", "Blue"),
        ("green", "Green"),
        ("red", "Red"),
        ("purple", "Purple"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default="yellow"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
