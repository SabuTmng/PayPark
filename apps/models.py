from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    UserId = models.AutoField(primary_key = True)
    FirstName = models.CharField(max_length = 30)
    LastName = models.CharField(max_length = 30)
    Email = models.CharField(max_length = 30)
    Contact = models.CharField(max_length = 10)
    District = models.CharField(max_length = 30)
    AddressLine1 = models.CharField(max_length = 30)
    AddressLine2 = models.CharField(max_length = 30)
    ZipCode = models.CharField(max_length = 10)
    IsAdmin = models.BooleanField(default = False)
    IsSuperAdmin = models.BooleanField(default = False)
    IsActive = models.BooleanField(default = False)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    Password = models.CharField(max_length=30)


class NoteModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notes"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title