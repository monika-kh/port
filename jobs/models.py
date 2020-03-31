from django.db import models


# Create your models here.
class Jobs(models.Model):
    job_name = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="media")

    def __str__(self):
        return self.job_name


class Apply(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)
    resume = models.FileField(upload_to="media/", max_length=254)
    job = models.ForeignKey(
        Jobs, on_delete=models.CASCADE, related_name="job", blank=True
    )

    def __str__(self):
        return self.name
