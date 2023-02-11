# fachschaft_informatik
## About this project
Web apps for the "Fachschaft Informatik" (Chritian Albrechts University, Kiel)

## Apps
### Kummerkasten
A simple form for anonymous email submissions. 
* [Website (english)](https://fachschaft-informatik-cau.onrender.com/kummerkasten/?lang=en)
* [Website (german)](https://fachschaft-informatik-cau.onrender.com/kummerkasten/?lang=de)

## Deployment
First off, you'll want to create a `/etc/secrets/email_config.json` file with your smtp credentials/configuration and set the necessary environment variables, namely `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS`.

**For deployment you'd create the following variables:**
```bash
SECRET_KEY=my_secret_random_django_key
DEBUG=False
ALLOWED_HOSTS=localhost,example.com
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

**"ALLOWED_HOSTS" might look something like this:**
```python
ALLOWED_HOSTS = ["my-domain.com", "1.1.1.1"]
```
