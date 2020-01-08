from datetime import date
from django.db import models
from django.db.models import F

from auditable.models import Auditable
from .organization_address import OrganizationAddress


class Organization(Auditable):
    """
    Contains a list of all of the recognized Part 3 fuel suppliers, both
    past and present, as well as an entry for the government which is also
    considered an organization.
    """
    name = models.CharField(
        max_length=500
    )

    @property
    def organization_address(self):
        """
        Gets the active address for the organization
        """
        data = OrganizationAddress.objects.filter(
            effective_date__lte=date.today(),
            organization_id=self.id
        ).exclude(
            expiration_date__lt=date.today()
        ).exclude(
            expiration_date=F('effective_date')
        ).order_by('-effective_date', '-update_timestamp').first()

        return data

    class Meta:
        db_table = 'organization'

    db_table_comment = "Contains a list of all of the recognized Part 3 " \
                       "fuel suppliers, both past and present, as well as " \
                       "an entry for the government which is also " \
                       "considered an organization."
