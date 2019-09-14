# -*- coding: utf-8 -*-

from django.db import models  # noqa: F401
from datetime import datetime
# Create your models here.


class Hour(models.Model):

    CLOCK_TYPES = (
        ('I', 'In'),
        ('O', 'Out'),
    )

    clock_type = models.CharField(
        max_length=1,
        choices=CLOCK_TYPES,
        default='I'
    )

    person = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
    )

    time = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.person.username + \
        '_' + self.clock_type + '_' + \
        datetime.now().strftime('%Y_%m_%d_%H_%m_%S') \
