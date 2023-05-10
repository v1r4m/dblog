from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Template(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    templateId = models.AutoField(primary_key=True)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class TextField(models.Model):
    templateId = models.ForeignKey(Template, on_delete=models.CASCADE)
    Xpos1 = models.IntegerField()
    Xpos2 = models.IntegerField()
    Ypos1 = models.IntegerField()
    Ypos2 = models.IntegerField()
    Question = models.TextField()

class SelectField(models.Model):
    templateId = models.ForeignKey(Template, on_delete=models.CASCADE)
    Question = models.TextField()

class Selection(models.Model):
    templateId = models.ForeignKey(Template, on_delete=models.CASCADE)
    fieldId = models.ForeignKey(SelectField, on_delete=models.CASCADE)
    optionDescription = models.TextField()
    Xpos1 = models.IntegerField()
    Xpos2 = models.IntegerField()
    Ypos1 = models.IntegerField()
    Ypos2 = models.IntegerField()
