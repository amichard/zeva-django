from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F, Q
import django.contrib.auth.validators

from auditable.models import Auditable


class UserProfile(Auditable):
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

    def natural_key(self):
        return (self.username,)

    class Meta:
        db_table = 'user'

    # Supplemental mapping for base class
    db_column_supplemental_comments = {
        'first_name': 'Django field. First name (retrieved from Siteminder',
        'last_name': 'Django field. Last name (retrieved from Siteminder)',
        'is_staff': 'Django field. Flag. True if staff user.',
        'is_superuser': 'Django field. Flag. True if superuser.',
        'is_active': 'Django field. True if can login.',
        'date_joined': 'Django field. Date account created.',
        'last_login': 'Django field. Last login time.',
    }

    db_table_comment = "Users who may access the application"
