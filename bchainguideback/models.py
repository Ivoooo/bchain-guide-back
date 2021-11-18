from django.db import models


# Create your models here.

# Entry some data into model
class UserData(models.Model):
    test_data = models.CharField(max_length=2000)

    # Create a string representation
    def __str__(self):
        return self.test_data
