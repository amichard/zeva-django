from rest_framework import serializers

from api.models.organization import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Supplier
    Loads most of the fields and the balance for the Supplier
    """

    class Meta:
        model = Organization
        fields = ('id', 'name', 'create_timestamp')
