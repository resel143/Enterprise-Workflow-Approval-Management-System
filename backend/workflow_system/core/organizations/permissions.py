from rest_framework.permissions import BasePermission
from .models import OrganizationMember

class IsOrganizationMember(BasePermission):
    def has_permission(self, request, view):
        org_id = request.headers.get('X-ORG-ID')
        if not org_id or not request.user.is_authenticated:
            return False
        
        return OrganizationMember.objects.filter(
            user=request.user,
            organization_id=org_id,
            is_active=True
        ).exists()