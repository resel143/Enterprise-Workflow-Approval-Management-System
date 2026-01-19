from django.db import models
from django.conf import settings
import uuid

class Organization(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=255, unique=True)
    slug=models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)


    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_organizations'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Department(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="departments"
    )
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)

    class Meta:
        unique_together = ('organization', 'name')

    def __str__(self):
        return f"{self.name} ({self.organization.name})"
    

class OrganizationMember(models.Model):

    ROLE_CHOICES = ( 
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('EMPLOYEE', 'Employee')
    )

    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user= models.ForeignKey(
         settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='memberships'
    )

    organization=models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='members'
    )

    department=models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    role= models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'organization')

    def __str__(self):
        return f"{self.user} - {self.organization} - {self.role} "



