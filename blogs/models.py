from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="media", blank=False)
    content = models.TextField()

    def __str__(self):
        return self.title

    def body(self):
        return self.content[:25]

    def date(self):
        return self.pub_date.strftime("%B %d %Y")
