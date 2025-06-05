from django.db import models
from apps.account.models import PartnerOrganization
from django.core.exceptions import ValidationError
import uuid

class StatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    APPROVED = 'APPROVED', 'Approved'
    REJECTED = 'REJECTED', 'Rejected'

class Application(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    EDUCATION_STATUS_CHOICES = [
        ('CURRENTLY_ENROLLED', 'Currently Enrolled'),
        ('FRESH_GRADUATE', 'Fresh Graduate'),
        ('GRADUATE', 'Graduate'),
        ('GAP_YEAR', 'Gap Year'),
    ]
    EXPERIENCE_LEVEL_CHOICES = [
        ('NONE', 'None'),
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    DATA_SCIENCE_LEVEL_CHOICES = [
        ('NONE', 'None'),
        ('BASIC', 'Basic'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    TIME_COMMITMENT_CHOICES = [
        ('1-2', '1-2'),
        ('3-5', '3-5'),
        ('6-10', '6-10'),
        ('11-15', '11-15'),
        ('16+', '16+'),
    ]

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    partner_org = models.ForeignKey(PartnerOrganization, on_delete=models.RESTRICT)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    country = models.CharField(max_length=100)
    state_region_province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    education_status = models.CharField(max_length=20, choices=EDUCATION_STATUS_CHOICES)
    institution_country = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=255)
    programming_experience = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES)
    data_science_experience = models.CharField(max_length=20, choices=DATA_SCIENCE_LEVEL_CHOICES)
    weekly_time_commitment = models.CharField(max_length=10, choices=TIME_COMMITMENT_CHOICES)
    scholarship_reason = models.TextField(max_length=1000)
    career_goals = models.TextField(max_length=500)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('email', 'partner_org')

    def __str__(self):
        return f"{self.email} ({self.partner_org.display_name})"

    def clean(self):
        if self.status not in StatusChoices.values:
            raise ValidationError('Invalid status.')

class ApplicationDemographic(models.Model):
    DEMOGRAPHIC_CHOICES = [
        ('UNEMPLOYED', 'Unemployed'),
        ('UNDEREMPLOYED', 'Underemployed'),
        ('BELOW_POVERTY', 'Below Poverty'),
        ('REFUGEE', 'Refugee'),
        ('DISABLED', 'Disabled'),
        ('STUDENT', 'Student'),
        ('WORKING_STUDENT', 'Working Student'),
        ('NONPROFIT_SCIENTIST', 'Nonprofit Scientist'),
    ]
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    demographic_group = models.CharField(max_length=30, choices=DEMOGRAPHIC_CHOICES)

    class Meta:
        unique_together = ('application', 'demographic_group')

    def __str__(self):
        return f"{self.application.email} - {self.demographic_group}"

class ApplicationDevice(models.Model):
    DEVICE_CHOICES = [
        ('SMARTPHONE', 'Smartphone'),
        ('LAPTOP', 'Laptop'),
        ('DESKTOP', 'Desktop'),
    ]
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=20, choices=DEVICE_CHOICES)

    class Meta:
        unique_together = ('application', 'device_type')

    def __str__(self):
        return f"{self.application.email} - {self.device_type}"

class ApplicationConnectivity(models.Model):
    CONNECTIVITY_CHOICES = [
        ('MOBILE_DATA', 'Mobile Data'),
        ('WIFI', 'WiFi'),
    ]
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    connectivity_type = models.CharField(max_length=20, choices=CONNECTIVITY_CHOICES)

    class Meta:
        unique_together = ('application', 'connectivity_type')

    def __str__(self):
        return f"{self.application.email} - {self.connectivity_type}"

class ApprovedApplicant(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    application = models.OneToOneField(Application, on_delete=models.RESTRICT)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Approved: {self.application.email}"
