import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	"""Django command to pause the execution until DB is available"""

	def handle(self, *args, **options):
		self.stdout.write("Waiting for DB")
		db_con = None
		while not db_con:
			try:
				db_con = connections['default']
			except:
				self.stdout.write("DB unavailable, waiting ...")
				time.sleep(1)
		
		self.stdout.write(self.style.SUCCESS('DB connected!'))
