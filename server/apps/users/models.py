from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    pass
    BRANCHES = (
        ('P', 'Programming'),
        ('E', 'Engineering'),
        ('B', 'Business'),
    )

    stud_id = models.IntegerField(null=True, blank=True)
    stud_id.verbose_name = "Student ID"
    stud_id.help_text = "Type in your 10-Digit ID. Used for logging attendance"
    branch = models.CharField(
        max_length=1,
        choices=BRANCHES,
        default=None,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
