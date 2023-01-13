from Crypto import Random
from Crypto.Cipher import AES
from django.core.management.base import BaseCommand
key = "a0e1c2dc40ea74eaf7784f4600884f6d" #128-ECB

#AES.MODE_ECB
class Command(BaseCommand):

	help = " AES encryption "

	def handle(self, **options):
		try:
			print("hii")
			# AES.MODE_CBC
			# obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
			iv = Random.new().read(AES.block_size)
			obj = AES.new('This is a key123', AES.MODE_ECB,iv)
			message = "The answer is no"
			
			ciphertext = obj.encrypt(message)
			print(ciphertext,"ciphertext")
			obj2 = AES.new('This is a key123', AES.MODE_ECB, iv)
			
			# AES.MODE_CBC
			decrypt = obj2.decrypt(ciphertext)
			print(decrypt," decrypt ")

		except Exception as e:
			print("bye")


