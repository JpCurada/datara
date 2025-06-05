from django.db import models
from apps.public.models import ApprovedApplicant, Application
from apps.account.models import PartnerOrganization
from django.core.exceptions import ValidationError
import uuid

class StatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'

class MoaSubmission(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    approved_applicant = models.OneToOneField(ApprovedApplicant, on_delete=models.RESTRICT)
    digital_signature = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)

    def __str__(self):
        return f"MoA: {self.approved_applicant.application.email} - {self.status}"

class Scholar(models.Model):
    id = models.CharField(primary_key=True, max_length=20, default=uuid.uuid4)  # SCHYYYYNNNN
    moa = models.OneToOneField(MoaSubmission, on_delete=models.RESTRICT)
    application = models.OneToOneField(Application, on_delete=models.RESTRICT)
    partner_org = models.ForeignKey(PartnerOrganization, on_delete=models.RESTRICT)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scholar: {self.id} ({self.application.email})"

class Certification(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_month = models.PositiveSmallIntegerField()
    issue_year = models.PositiveSmallIntegerField()
    expiration_month = models.PositiveSmallIntegerField(blank=True, null=True)
    expiration_year = models.PositiveSmallIntegerField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True, null=True)
    credential_url = models.URLField(max_length=500, blank=True, null=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.scholar.id})"

    def clean(self):
        if self.expiration_year and self.expiration_month:
            if (self.expiration_year < self.issue_year) or (
                self.expiration_year == self.issue_year and self.expiration_month < self.issue_month):
                raise ValidationError('Expiration date must be after issue date.')

class Job(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    testimonial = models.TextField(max_length=2000, blank=True, null=True)
    media_file = models.FileField(upload_to='job_media/', blank=True, null=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.job_title} at {self.company} ({self.scholar.id})"
