#sent_turtle
class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=None):
        """Read messages from the user's inbox.

        :param str username: The username whose inbox will be read.
        :param int n: The number of messages to read. If not provided, read all messages.
        :return: A list of messages.
        :rtype: list
        :raises KeyError: if the username does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f'User {username} does not exist.')

        user_box = self.boxes[username]
        if n is None:
            messages = user_box[:]
            self.boxes[username] = []
        else:
            messages = user_box[:n]
            self.boxes[username] = user_box[n:]
        return messages

    def search_inbox(self, username, search_string):
        """Search for messages in the user's inbox containing the search string.

        :param str username: The username whose inbox will be searched.
        :param str search_string: The string to search for in the messages.
        :return: A list of messages containing the search string.
        :rtype: list
        :raises KeyError: if the username does not exist.
        """
        if username not in self.boxes:
            raise KeyError(f'User {username} does not exist.')

        user_box = self.boxes[username]
        matching_messages = [
            message for message in user_box
            if search_string in message['body']
        ]
        return matching_messages
