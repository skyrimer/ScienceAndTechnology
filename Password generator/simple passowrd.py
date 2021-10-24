# first method
import secrets
import random
from string import ascii_letters, punctuation, digits
length = 30
choice = ascii_letters + punctuation + digits
password = ''.join(random.sample(choice, length))
print(password)

# second method
print(secrets.token_hex(10))
