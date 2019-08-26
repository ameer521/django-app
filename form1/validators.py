from django.core.exceptions import ValidationError

def validate_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("Validation Error")