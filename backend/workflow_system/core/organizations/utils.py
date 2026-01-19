from .models import Organization, OrganizationMember


def get_active_organization(request):
    org_id = request.headers.get('X-ORG-ID')
    if not org_id:
        return None
    
    try:
        return Organization.objects.get(id=org_id, is_active=True)
    except Organization.DoesNotExist:
        return None
