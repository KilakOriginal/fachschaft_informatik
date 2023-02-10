from django import forms
from django.db import models

class Email(models.Model):
    '''Define form data'''
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=5000)

class EmailForm(forms.ModelForm):
    '''Store form data'''
    class Meta:
        model = Email
        fields = ["subject", "message"]

# Locate this file
import os.path
dir_path = os.path.dirname(os.path.realpath(__file__))

def send_mail(to: str, subject: str, message: str, configuration_file: str = f"/etc/secrets/email_config.json"):
    '''Send an email - to: Recipient, subject: Subject line, message: Email body, configuration_file: .json-file path containing configuration data'''
    configuration = {}  # Contains configuration data
    import smtplib, ssl, json
    from socket import gaierror

    # Load configuration file contents into dict
    with open(configuration_file) as f:
        configuration = json.loads(f.read())

    context = ssl.create_default_context()  # Create SSL context

    # Try sending an email
    try:
        with smtplib.SMTP_SSL(configuration["smtp_address"], configuration["port"], context=context) as server:
            server.login(configuration["user"], configuration["password"])  # Log into the service using configuration data
            server.sendmail(configuration["user"], to , f'Subject: [Kummerkasten] {subject}\n\n{message}'.encode("utf-8"))  # Send email
        return 0  # OK
    except (gaierror, ConnectionRefusedError):  # Unable to connect to the server specified in the configuration file
        print('Failed to connect to the server. Bad connection settings?')
        return -1  # Error
    except smtplib.SMTPServerDisconnected:  # Unable to maintain connection; usually authentication error (username/password)
        print('Failed to connect to the server. Wrong user/password?')
        return -1  # Error
    except smtplib.SMTPException as e:  # Unable to send email for some other reason
        print('SMTP error occurred: ' + str(e))
        return -1  # Error
