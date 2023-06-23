from django.db import models
class User(models.Model):
    userID = models.CharField(max_length=255)
    userPW = models.CharField(max_length=255)

    def __str__(self):
        return self.userID
        return self.userPW
    class Meta:
        app_label = 'myapp'

