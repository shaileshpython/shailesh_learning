from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import base64

def encrypt(msg,key):
	msg = pad(msg.encode(),32)
	cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
	return base64.b64encode(cipher.encrypt(msg))
	

def decrypt(encrypted_msg,key):
	enc = base64.b64decode(encrypted_msg)
	cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
	decrypt_json = unpad(cipher.decrypt(enc),32)
	return decrypt_json.decode("utf8")

def encrypt_cbc(msg,key):
	msg = pad(msg.encode(),32)
	cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
	return base64.b64encode(cipher.encrypt(msg))

def decrypt_cbc(encrypted_msg,key):
	enc = base64.b64decode(encrypted_msg)
	cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
	decrypt_json = unpad(cipher.decrypt(enc),32)
	return decrypt_json.decode("utf8")