from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        email = {}
        email['from'] = self.cleaned_data.get('email')
        email['subject'] = '[site-cal] ' + self.cleaned_data.get('subject')
        email['phone'] = self.cleaned_data.get('phone')
        email['message'] = self.cleaned_data.get('message')
        email['name'] = self.cleaned_data.get('name')
        html_message = render_to_string('email/contact.html', email)
        return send_mail(
            email['subject'], email['message'], 'application@aikidoleoni.org',
            ['contato@aikidoleoni.org'], html_message=html_message,
            fail_silently=False
        )
