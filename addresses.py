from fbchat import Client
from unidecode import unidecode
from config import EMAIL, PASSWORD

client = Client(EMAIL, PASSWORD)

# Fetches a list of all users you're currently chatting with, as `User` objects
users = client.fetchAllUsers()

"""
for user in users:
    name = unidecode(user.name).lower()
    if "michal" in name:
        print(f"{user.uid}: {user.name}")
"""

# client.logout()
