#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Profession_analytics.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

import csv
import datetime
from django.core.management.base import BaseCommand
from pages.models import Job

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('vacancies.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                job = Job(
                    name=row['name'],
                    key_skills=row['key_skills'],
                    salary_from=float(row['salary_from']) if row['salary_from'] else None,
                    salary_to=float(row['salary_to']) if row['salary_to'] else None,
                    salary_currency=row['salary_currency'],
                    area_name=row['area_name'],
                    published_at=datetime.datetime.strptime(row['published_at'], '%Y-%m-%dT%H:%M:%S%z')
                )
                job.save()