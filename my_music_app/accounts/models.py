from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


def validate_password(value):
    for ch in value:
        if not ch.isalpha() and not ch.isdigit() and not ch == '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(max_length=30, validators=[
            MinLengthValidator(2, 'the field must contain at least 50 characters'), validate_password
            ])
    email = models.EmailField(null=True)

    age = models.PositiveIntegerField(blank=True, null=True)