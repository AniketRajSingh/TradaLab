from django.contrib import admin
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import OfferLetter
from django import forms
from django.contrib.auth.models import User
from django.template import Context
from io import BytesIO
from xhtml2pdf import pisa
from django.core.files.base import ContentFile
from datetime import date

class OfferLetterAdminForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'select2'}),
    )
    class Meta:
        model = OfferLetter
        fields = ('users',)

class OfferLetterAdmin(admin.ModelAdmin):
    form = OfferLetterAdminForm
    list_display = ('subject',)

    def save_model(self, request, obj, form, change):
        subject = "Congratulations! Your Internship Request Has Been Accepted 🎉"
        users = form.cleaned_data.get('users')
        html_template = 'offer_letter/offer_letter.html'
        pdf_template = 'offer_letter/OfferLetter.html'
        recipient_emails = [user.email for user in users]

        # Fetch user details from the database
        user_details = users.values('username', 'first_name', 'last_name')
        
        # Generate the ref_id
        user_ids = users.values_list('id', flat=True)
        ref_id = f"TRA/OFL/{date.today().strftime('%Y%m')}/{'_'.join(map(str, user_ids))}"

        # Render HTML template with context
        context = {
            'subject': subject,
            'date': date.today(), 
            'recipient_emails': recipient_emails,
            'user_details': user_details,
            'ref_id':ref_id
        }
        rendered_html = render_to_string(html_template, context)
        pdf_html = render_to_string(pdf_template, context)

        # Convert HTML to PDF using xhtml2pdf
        pdf_file = BytesIO()
        pisaStatus = pisa.CreatePDF(pdf_html, dest=pdf_file)

        if pisaStatus.err:
            raise Exception(f"HTML to PDF conversion failed: {pisaStatus.err}")

        # Save the PDF as a ContentFile
        pdf_file.seek(0)
        pdf_content = pdf_file.read()

        # Send email with HTML content and attached PDF
        email = EmailMultiAlternatives(subject, strip_tags(rendered_html), 'letter@tradalab.tech', recipient_emails)
        email.attach_alternative(rendered_html, "text/html")
        email.attach('offer_letter.pdf', pdf_content, 'application/pdf')
        email.send()

        obj.save()

admin.site.register(OfferLetter, OfferLetterAdmin)
