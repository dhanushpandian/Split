import secrets
import string

def generate_short_code(length=5):
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    return ''.join(secrets.choice(characters) for _ in range(length))

code = generate_short_code()
print("Session Code:", code)
