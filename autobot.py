from fbchat import Client  # , log
from fbchat.models import Message

from datetime import datetime


class AutoBot(Client):

    def listen(self, markAlive=None):
        if markAlive is not None:
            self.setActiveStatus(markAlive)

        self.startListening()
        self.onListening()

        recipient_id = self.uid
        counter = 5
        previous = None
        while self.listening and self.doOneListen():
            if counter <= 0:
                break

            now = datetime.now()
            if previous is not None and now.second == previous.second:
                continue

            actual_time = f"{now.hour}:{now.minute:02}:{now.second:02}"
            print(actual_time)
            self.send(Message(actual_time), recipient_id)

            previous = now
            counter -= 1

        self.stopListening()
