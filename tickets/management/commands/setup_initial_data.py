from django.core.management.base import BaseCommand
from tickets.models import Column, Priority, RequestType


class Command(BaseCommand):
    help = 'Creates initial columns, priorities, and request types'

    def handle(self, *args, **kwargs):
        # Create default columns
        columns = ['Backlog', 'In Progress', 'Done']
        for col_name in columns:
            Column.objects.get_or_create(status=col_name)
            self.stdout.write(self.style.SUCCESS(f'Created column: {col_name}'))

        # Create priorities
        priorities = [
            ('Critical', 100),
            ('High', 80),
            ('Medium', 50),
            ('Low', 20),
        ]
        for name, score in priorities:
            Priority.objects.get_or_create(name=name, defaults={'score': score})
            self.stdout.write(self.style.SUCCESS(f'Created priority: {name}'))

        # Create request types
        request_types = ['Bug', 'Feature', 'Enhancement', 'Task', 'Documentation']
        for req_type in request_types:
            RequestType.objects.get_or_create(type=req_type)
            self.stdout.write(self.style.SUCCESS(f'Created request type: {req_type}'))

        self.stdout.write(self.style.SUCCESS('Initial data setup complete!'))
