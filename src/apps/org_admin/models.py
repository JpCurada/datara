from django.db import models
from apps.public.models import Application
from apps.account.models import Admin
from apps.scholar.models import MoaSubmission
import uuid

class StatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'

class ApplicationReview(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    application = models.ForeignKey(Application, on_delete=models.RESTRICT)
    admin = models.ForeignKey(Admin, on_delete=models.RESTRICT)
    action = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    action_reason = models.TextField(blank=True, null=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review: {self.application.email} by {self.admin.email} - {self.action}"

class MoaReview(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    moa = models.ForeignKey(MoaSubmission, on_delete=models.RESTRICT)
    admin = models.ForeignKey(Admin, on_delete=models.RESTRICT)
    action = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    action_reason = models.TextField(blank=True, null=True)
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MoA Review: {self.moa.id} by {self.admin.email} - {self.action}"
