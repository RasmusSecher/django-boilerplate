from django.db import models


class Document(models.Model):
    file = models.FileField()
    executionTime = models.TextField(default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name}"


class Attribute(models.Model):
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="attributes"
    )

    name = models.TextField(default="")
    type = models.TextField()
    regex = models.TextField()
    security = models.IntegerField()
    security_manual = models.BooleanField(default=False)
