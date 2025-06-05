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
        )

        self.stdout.write("Company and admin user created")
