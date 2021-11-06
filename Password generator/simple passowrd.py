import secrets
import random
from string import ascii_letters, digits
length = 30
choice = ascii_letters + digits

# first method
print(''.join(random.sample(choice, length)))

# second method
print(''.join(random.choice(choice) for _ in range(length)))

# third method
print(''.join(secrets.choice(choice) for _ in range(length)))

# forth method
print(secrets.token_hex(length))














