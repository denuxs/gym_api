MALE = "male"
FEMALE = "female"

GENDER_CHOICES = (
    (MALE, "Hombre"),
    (FEMALE, "Mujer"),
)

COACH = "coach"
CLIENT = "client"

USER_TYPES_CHOICES = (
    (COACH, "Entrenador"),
    (CLIENT, "Cliente"),
)

DAYS_OF_WEEK = (
    (1, "Lunes"),
    (2, "Martes"),
    (3, "Miercoles"),
    (4, "Jueves"),
    (5, "Viernes"),
    (6, "Sabado"),
    (7, "Domingo"),
)

BEGINNER = "beginner"

WORKOUT_LEVEL = (
    ("beginner", "Principiante"),
    ("medium", "Medio"),
    ("advanced", "Avanzado"),
)

WORKOUT_GOAL = (
    ("gain_muscle", "Ganar Musculo"),
    ("strength", "Fuerza"),
    ("lose_weight", "Perder Peso"),
)


KEY_CHOICES = (
    ("muscle", "Musculo"),
    ("equipment", "Equipo"),
)
