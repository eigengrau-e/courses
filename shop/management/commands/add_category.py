from django.core.management.base import BaseCommand, CommandError

from shop.models import Category


class Command(BaseCommand):
    help = 'Add a new category'

    def handle(self, *args, **options):
        category_title = input("Enter category title:")

        category, created = Category.objects.get_or_create(title=category_title)
        if not created:
            raise CommandError("Category already exists")

        self.stdout.write("Added new category")
