import string
import secrets

chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '%&$#()'
size = 12

for i in range(10):
   print(''.join(secrets.choice(chars) for x in range(size)))
