from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser

# Create your models here.
# Reader -> AbstractUser -> AbstractBaseUser -> models.Model
class Reader(AbstractUser):# instead of Reader(models.Model)
    READER_TITLE = {
        # key= will be stored in the database
        # value = will be displayed to the user
        "Mr": "Mr",
        "Mrs": "Mrs",
        "Ms": "Ms",
        "Dr": "Dr"
    }
    # If no explicit primary key is defined, Django will generate an id for us.
    # Class attributes will represent fields in our table.
    # By default, Django fields are 'not null'.
    username = models.CharField(max_length=50, primary_key=True)
    # null=True set the null field when used on the terminal
    # blank=True set the null field when used on the dashboard
    title = models.CharField(max_length=5, null=True, blank=True, choices=READER_TITLE)
    # If you want toremove default ,just set it to None.
    # email = None

    class Meta:
        # Define some meta data, including constraints
        constraints = [
            models.CheckConstraint(
                # reader_Reader_title_check
                name='%(app_label)s_%(class)s_tittle_check', # unique key
                check=models.Q(title__in=['Mr', 'Mrs', 'Ms', 'Dr'])
            )
        ]