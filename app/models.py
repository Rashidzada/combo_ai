from django.db import models

class AITool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name