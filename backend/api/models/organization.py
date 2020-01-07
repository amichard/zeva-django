from datetime import date
from django.db import models
from django.db.models import F

from auditable.models import Auditable


class Organization(Auditable):
    """
    Contains a list of all of the recognized Part 3 fuel suppliers, both
    past and present, as well as an entry for the government which is also
    considered an organization.
    """
    name = models.CharField(
        max_length=500
    )

    class Meta:
        db_table = 'organization'

    db_table_comment = "Contains a list of all of the recognized Part 3 " \
                       "fuel suppliers, both past and present, as well as " \
                       "an entry for the government which is also " \
                       "considered an organization."
