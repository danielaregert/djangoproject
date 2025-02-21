### First steps
install myenv
create myenvdani
install python
install django
clone this repo

## Activate virtual enviroment
> source myenvdani/Scripts/activate

## Run server
open the folder mydojangoproject
> python manage.py runserver

### Important comands
## before creating models
> python manage.py makemigrations
> python manage.py migrate

## open django shell
> python manage.py shell

## creating superuser
from django.contrib.auth.models import User
User.objects.create_superuser('username', 'email@email.com', 'yourpassword')

## set the mail .env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=yourmail@gmail.com
EMAIL_HOST_PASSWORD='your_password'

## in production:
> python manage.py collectstatic
## local 
> http://127.0.0.1:8000/