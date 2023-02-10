# fachschaft_informatik
## About this project
Web apps for the "Fachschaft Informatik" (Chritian Albrechts University, Kiel)

## Apps
### Kummerkasten
A simple form for anonymous email submissions. I might also permit/implement file uploads in the future.

## Deployment
First off, you'll want to create a `/etc/secrets/email_config.json` file with your smtp credentials/configuration and set the necessary environment variables, namely `SECRET_KEY` and `DEBUG`.

**For deployment you'd create the following variables:**
```bash
SECRET_KEY=my_secret_random_django_key
DEBUG=False
```

**"email_config.json" might look something like this:**
```json
{
   "port":465,
   "smtp_address":"smtp.example.com",
   "user":"user-123@example.com",
   "password":"my_password"
}
```

Before deploying, remember to [set up your server to handle static files](https://docs.djangoproject.com/en/4.1/howto/static-files/deployment/) **or** alternatively run 
```python 
python manage.py runserver [YOUR_IP]:[PORT] --insecure
```
from the source directory (**NOT** recommended!). Another option still for serving your static files would be [AWS](https://aws.amazon.com/) or similar services if you do not wish to host them on your own server. For more info see [deployment checklist](https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/).

You will need to add your server to the `ALLOWED_HOSTS` list in the settings file located at `/%project_source%/fachschaft_informatik/settings.py`.

**"ALLOWED_HOSTS" might look something like this:**
```python
ALLOWED_HOSTS = ["my-domain.com", "1.1.1.1"]
```
