from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import secrets

class Folder(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # Kis Admin ne ye folder banaya
    master_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folders')
    # Parent folder (NULL => root folder for this master)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    def __str__(self):
        return self.name
    
class SharedFile(models.Model):
    # Master user (Admin)
    master_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='master_files')
    
    # Folder connection (Nullable rakha hai taake file bahar bhi ho sakay)
    # If a folder is deleted, delete its files too (matches "delete folder and everything inside").
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True, related_name='files')
    
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    upload_time = models.DateTimeField(auto_now_add=True)
    # Calendar-based expiry (chosen by master). If NULL, we fall back to duration_hrs.
    expiry_at = models.DateTimeField(null=True, blank=True)
    duration_hrs = models.IntegerField(default=2) 
    
    # Clients jinhe file nazar aayegi
    allowed_users = models.ManyToManyField(User, related_name='shared_with_me')

    @property
    def is_editable(self):
        # Time check logic
        expiry = self.expiry_at if self.expiry_at else (self.upload_time + timedelta(hours=self.duration_hrs))
        return timezone.now() < expiry

    def __str__(self):
        return self.title

    def get_expiry_timestamp(self):
        # Milliseconds mein expiry time JS timer ke liye
        expiry = self.expiry_at if self.expiry_at else (self.upload_time + timedelta(hours=self.duration_hrs))
        return int(expiry.timestamp() * 1000)

    class Meta:
        ordering = ['-upload_time'] # Nayi files hamesha upar nazar aayengi


class PasswordResetRequest(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_INFORMED = 'informed'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_INFORMED, 'Informed'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    requested_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='password_reset_requests',
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    master_note = models.TextField(blank=True, default='')
    executed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Password reset for {self.requested_user.username} ({self.status})'

    @staticmethod
    def generate_temporary_password(length: int = 14) -> str:
        # Token provides randomness; length is best-effort for UX.
        return secrets.token_urlsafe(length)[:length]