## AFIT API

API REST para crear rutinas de gimnasio. (**En desarrollo**)

### Paquetes

- Django 5
- Django Rest Framework
- Simple JWT
- Firebase
- Sqlite/Postgres
- Swagger
- Firebase

### Funcionalidades

- Autenticación JWT
- CRUD de usuarios
- CRUD de catálogos
- CRUD de ejercicios
- CRUD de rutinas
- CRUD de medidas
- Comentarios
- Publicaciones
- Subida de Imágenes
- Notificaciones Push
- Traducción 118n

### Ejecutar app

```
pip install -r requirements.txt

Renombrar archivo .example a .env y configurar variables de entorno

python manage.py migrate
python manage.py runserver

python manage.py loaddata catalogs.json
```

### TO DO
- Autenticación con cookies
- Unit Tests