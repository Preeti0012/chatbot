from django.db import models

class User(models.Model):
    USER_TYPES = [
        ('user', 'User'),
        ('persona', 'Persona'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=USER_TYPES)
    specialisation = models.CharField(max_length=255, blank=True, null=True)
    similar_attribute = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





