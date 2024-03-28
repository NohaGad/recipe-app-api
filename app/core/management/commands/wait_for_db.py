"""
Django command to wait for the database to be available.
"""
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """ Django command to wait for database. """

    def handle(self, *args, **options):
        """ Command to handle wait for database untill it is ready. """

        self.stdout.write('Checking if database is up ...')
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Waiting for database ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available!'))
