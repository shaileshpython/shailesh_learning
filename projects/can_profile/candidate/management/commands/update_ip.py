from django.core.management.base import BaseCommand

class Command(BaseCommand):

	help = "Alternate number update"

	def handle(self, **options):
		try:
			ip = input("Enter ur new ip : ")
			#update at /etc/environment ,/etc/default/fl
			# open file 
			# opening the file in read mode
			f = open("/etc/environment", "r")
			# f is the File Handler
			
			# check the file is open
			# calling read() function using file handler "f"

			print(f.read())
			print("try")

		except Exception as e:
			
			print("error at ip script ",e)
