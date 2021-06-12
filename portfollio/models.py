from django.db import models

class Project(models.Model):
    title = models.CharField( max_length=150)
    image = models.ImageField( upload_to='media')
    description = models.TextField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return str(self.id)
