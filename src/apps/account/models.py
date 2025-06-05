from django.db import models
from django.core.exceptions import ValidationError
import uuid
from django.contrib.auth.hashers import make_password, check_password

class PartnerOrganization(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    display_name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='org_logos/', blank=True, null=True)
    moa_document = models.FileField(upload_to='org_moas/', blank=True, null=True)
    support_email = models.EmailField()
    available_slots = models.PositiveIntegerField(default=0)
    is_accepting = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name

    def clean(self):
        if self.available_slots < 0:
            raise ValidationError('Available slots cannot be negative.')

class Admin(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    partner_org = models.ForeignKey(PartnerOrganization, on_delete=models.RESTRICT, related_name='admins')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.partner_org and self.partner_org.admins.exclude(pk=self.pk).count() >= 2:
            raise ValidationError('A PartnerOrganization can have at most 2 Admins.')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
