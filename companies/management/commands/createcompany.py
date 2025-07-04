from django.core.management.base import BaseCommand

from companies.models import Company
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Create a company and admin user"

    def handle(self, *args, **options):
        model = Company.objects.create(name="AFIT")

        User.objects.create_superuser(
            "admin",
            "admin@afit.com",
            "endurance",
            first_name="admin",
            last_name="admin",
            company=model,
            role="admin",
        )

        User.objects.create_user(
            "coach",
            "coach@afit.com",
            "demodemo25",
            first_name="coach",
            last_name="demo",
            company=model,
            role="coach",
        )

        User.objects.create_user(
            "client",
            "client@afit.com",
            "demodemo25",
            first_name="client",
            last_name="demo",
            company=model,
            role="client",
        )

        self.stdout.write("Company and users created")
