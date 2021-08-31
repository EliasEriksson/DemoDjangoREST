from django.db import models

# Create your models here.


class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=128)
    progression = models.CharField(max_length=1)
    plan = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"code={self.code}, " \
               f"name={self.name}, " \
               f"progression={self.progression}, " \
               f"plan={self.plan})"

