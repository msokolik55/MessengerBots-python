from fbchat import Client  # , log


class Reply:
    def __init__(self, keys, output):
        self.keys = keys
        self.output = output


class EchoBot(Client):
    goodNight = Reply(["dobru noc"], "dobru noc ;*")
    goodMorning = Reply(["dobre rano", "dobre ranko"], "dobre rano prajem :)")
    goodAfternoon = Reply(["dobry den"], "dobry den prajem :D")
    goodEvening = Reply(["dobry vecer"], "dobry vecer prajem ;)")
    replies = [goodMorning, goodAfternoon, goodEvening, goodNight]

    def generateOutput(self, message):
        for reply in self.replies:
            if message in reply.keys:
                return reply.output
        return ""

    def onMessage(self, author_id, message_object, thread_id, thread_type,
                  **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        # log.info(
        #     f"text: {message_object.text}\n" +
        #     f"from {thread_id}\n" +
        #     f"in {thread_type.name}")

        msg_text = message_object.text.lower()
        reply = self.generateOutput(msg_text)

        # If you're not the author, echo
        if (author_id != self.uid) and (len(reply) > 0):
            message_object.text = reply
            self.send(message_object, thread_id=thread_id,
                      thread_type=thread_type)
