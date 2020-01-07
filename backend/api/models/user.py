from django.db import models
from django.db.models import F, Q
import django.contrib.auth.validators

from auditable.models import Auditable


class User(Auditable):
    """
    User Model
    """
    email = models.EmailField(
        blank=True,
        null=True,
        db_comment="Primary email address"
    )
    organization = models.ForeignKey(
        'Organization',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    phone = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        db_comment="Primary phone number"
    )
    title = models.CharField(
        blank=True,
        max_length=100,
        null=True,
        db_comment="Professional Title"
    )

    class Meta:
        db_table = 'user'

    db_table_comment = "Users who may access the application"
