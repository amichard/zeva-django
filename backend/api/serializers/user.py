from rest_framework import serializers

from api.models.user_profile import UserProfile
from .organization import OrganizationSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the full details of the User and what permissions
    the user has
    """
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            'id', 'first_name', 'last_name', 'email',
            'username', 'display_name', 'is_active',
            'organization', 'phone')
