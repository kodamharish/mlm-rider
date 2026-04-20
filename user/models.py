from django.db import models

# Create your models here.
# riders/models.py
from django.db import models


def rider_upload_path(instance, filename):
    return f"riders/{instance.id}/{filename}"


class Rider(models.Model):

    VEHICLE_CHOICES = (
        ('bike', 'Bike'),
        ('scooter', 'Scooter'),
        ('cycle', 'Cycle'),
        ('car', 'Car'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    # 🔹 Personal Info
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    aadhaar_number = models.CharField(max_length=12, unique=True)

    # 🔹 Contact Info
    mobile_number = models.CharField(max_length=10)
    alternate_mobile_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(unique=True)
    emergency_contact_number = models.CharField(max_length=10)

    # 🔹 Address Info
    residential_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    # 🔹 Bank Details
    account_holder_name = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)

    # 🔹 Vehicle & Documents
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_CHOICES)
    vehicle_number = models.CharField(max_length=20, unique=True)  # ✅ UNIQUE

    driving_license_number = models.CharField(max_length=50)
    license_valid_upto = models.DateField()

    pan_card_number = models.CharField(max_length=10)

    # 🔹 File Uploads
    aadhaar_image = models.ImageField(upload_to=rider_upload_path, blank=True, null=True)
    dl_image = models.ImageField(upload_to=rider_upload_path, blank=True, null=True)

    # 🔹 Referral
    referral_id = models.CharField(max_length=20, blank=True, null=True)

    # 🔹 Agreements
    is_info_correct = models.BooleanField(default=False)
    is_terms_accepted = models.BooleanField(default=False)

    # 🔹 Status
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.vehicle_number})"