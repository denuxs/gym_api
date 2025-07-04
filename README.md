## AFIT API

API REST para crear rutinas de gimnasio. (**En desarrollo**)

El Frontend esta en Angular 18 [github.com/denuxs/afit-admin](https://github.com/denuxs/afit-admin)

### Paquetes

- Django 5
- Django Rest Framework
- Simple JWT
- Firebase
- Sqlite/Mysql
- Swagger

### Funcionalidades

- Autenticación JWT
- API usuarios(admin,entrenadores,clientes)
- API catálogos
- API ejercicios
- AP rutinas
- API medidas
- Subida de Imágenes a S3
- Traducción 118n

### Base datos

![`Database`](https://github.com/denuxs/gym_api/blob/main/afit.png)

### Ejecutar app

```
pip install -r requirements.txt

Renombrar archivo .example a .env y configurar variables de entorno

python manage.py migrate
python manage.py createcompany #crea una empresa y usuarios por defecto
python manage.py runserver

```

### TO DO
- Autenticación con cookies
- Unit Tests