## AFIT API

API REST para crear rutinas de gimnasio. (**En desarrollo**)

### Paquetes

- Django 5
- Django Rest Framework
- Django Rest Simple JWT
- Firebase

### Funcionalidades

- Autenticación JWT
- CRUD de usuarios
- CRUD de equipos
- CRUD de ejercicios
- CRUD de rutinas

### Ejecutar app

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

python manage.py loaddata catalogs.json
```

### TO DO
- Refactorizar código
- Autenticación con cookies
- Unit Tests