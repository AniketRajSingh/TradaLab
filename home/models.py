from django.db import models

class InternApplication(models.Model):
    name = models.CharField(max_length=100)
    domain_choices = [
        ('web', 'Web Development'),
        ('app', 'App Development'),
        ('ml', 'Machine Learning'),
        # Add more choices as needed
    ]
    desired_domain = models.CharField(max_length=10, choices=domain_choices)
    email = models.EmailField()
    qualification = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
