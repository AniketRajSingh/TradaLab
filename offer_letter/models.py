from django.db import models
from datetime import date

class OfferLetter(models.Model):
    subject = models.CharField(max_length=200)
    users = models.ManyToManyField('auth.User', blank=True)
    use_html_template = models.BooleanField(default=False)
    html_template = models.FileField(upload_to='offer_letter_templates/', null=True, blank=True)
    date = models.DateField(default=date.today)
    ref_id = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.subject
