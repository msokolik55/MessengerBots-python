from echobot import EchoBot
from config import EMAIL, PASSWORD

client = EchoBot(EMAIL, PASSWORD)
client.listen()
