from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if not user.is_staff:
            user.is_verified = False
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
          """
          Create and save a SuperUser with the given email and password.
          """
          extra_fields.setdefault('is_staff', True)
          extra_fields.setdefault('is_admin', True)
          extra_fields.setdefault('is_superuser', True)
          extra_fields.setdefault('is_active', True)

          if extra_fields.get('is_staff') is not True:
              raise ValueError(('Superuser must have is_staff=True.'))
          if extra_fields.get('is_superuser') is not True:
              raise ValueError(('Superuser must have is_superuser=True.'))
          return self.create_user(email, password, **extra_fields)


    def authenticate(self, request, email, password):
        from django.contrib.auth import authenticate
        user = authenticate(request, email=email, password=password)
        return user
