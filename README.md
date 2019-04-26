# myacademic-back

## Tecnologias
- django 2.2
- postgres 9.6
- django-rest-framework

## Instalação

Para qualquer sistema operacional:

```sh
virtualenv -p /usr/bin/python3 myacademic-env

source myacademic-env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

access http://localhost:8000
```