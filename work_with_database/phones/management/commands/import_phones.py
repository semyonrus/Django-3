from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify
import csv


class Command(BaseCommand):
    help = 'Imports phones from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **options):
        file_path = options['csv_file_path']

        with open(file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            next(csvreader)  # Пропускаем заголовок

            for row in csvreader:
                _, created = Phone.objects.update_or_create(
                    id=row[0],
                    defaults={
                        'name': row[1],
                        'price': float(row[3]),
                        'slug': slugify(row[1]),
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added phone {row[1]}'))
                else:
                    self.stdout.write(f'Phone {row[1]} already exists')