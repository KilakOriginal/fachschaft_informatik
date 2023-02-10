# fachschaft_informatik
## About this project
Web apps for the "Fachschaft Informatik" (Chritian Albrechts University, Kiel)

## Apps
### Kummerkasten
A simple form for anonymous email submissions. I might also permit/implement file uploads in the future.

## Deployment
Make sure to create the </src/kummerkasten/email_config.json> and </src/fachschaft_informatik/secret_key.txt> files with your smtp credentials/configuration and desired key respectively.

**"email_config.json" might look something like this:**
```json
    {
      "port":465,
      "smtp_address":"smtp.example.com",
      "user":"user-123@example.com",
      "password":"my_password"
    }
```

**"secret_key.txt" might look something like this:**
```
    my_secret_django_key
```

Before deploying, make sure to set up your server to handle the static files **or** alternatively run 
```python 
    python manage.py [YOUR_IP]:[PORT] --insecure
```
from the source directory (**NOT** recommended!). For more info see [deployment checklist](https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/).

You will need to add your server to the "ALLOWED_HOSTS" list in the settings.py file located at /src/fachschaft_informatik/settings.py.

**"ALLOWED_HOSTS" might look something like this:**
```python
    ALLOWED_HOSTS = ["my-domain.com", "1.1.1.1"]
```
