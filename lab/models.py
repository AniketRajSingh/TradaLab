from django.db import models

class LabExperiment(models.Model):
    STANDARD_CHOICES = [
        ('10th', 'Class 10th'),
        ('12th', 'Class 12th'),
        ('engineering', 'Engineering'),
    ]
    SUBJECT_CHOICES = [
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('maths', 'Mathematics'),
        ('electronics', 'Electronics'),
        ('mechanical', 'Mechanical'),
        ('civil', 'Civil'),
    ]

    standard = models.CharField(max_length=20, choices=STANDARD_CHOICES)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    experiment = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.URLField()
    experiment_url = models.CharField(max_length=100)
    experiment_css_url = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.standard} - {self.experiment}"
