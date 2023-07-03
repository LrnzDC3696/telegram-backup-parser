__all__ = ("TextEntity", "Message", "Chat")

from typing import List


class TextEntity:
    """A class representing text entities.

    Attributes
    ----------
    type_ : str
        The type of the text entity.
    text : str
        The text content of the entity.

    Methods
    -------
    __init__(type_, text)
        Initializes a new instance of TextEntity.
    __repr__()
        Returns a string representation of the TextEntity instance.
    __str__()
        Returns a string representation of the TextEntity instance.
    from_dict(data)
        Creates a new TextEntity instance from a dictionary.

    """

    __slots__ = ('type_', 'text')

    def __init__(self, type_, text):
        """
        Initializes a new instance of the TextEntity class.

        Parameters
        ----------
        type_ : str
            The type of the text entity.
        text : str
            The text content of the entity.

        """
        self.type_ = type_
        self.text = text

    def __repr__(self):
        """
        Returns a string representation of the TextEntity instance.

        Returns
        -------
        str
            A string representation of the TextEntity instance.

        """
        return f"TextEntity(type_='{self.type_}', text='{self.text}')"

    def __str__(self):
        """
        Returns a string representation of the TextEntity instance.

        Returns
        -------
        str
            A string representation of the TextEntity instance.

        """
        return f"Type: {self.type_}, Text: {self.text}"

    @classmethod
    def from_dict(cls, data):
        """
        Creates a new TextEntity instance from a dictionary.

        Parameters
        ----------
        data : dict
            The dictionary containing 'type' and 'text' keys.

        Returns
        -------
        TextEntity
            A new TextEntity instance.

        """
        return cls(type_=data['type'], text=data['text'])


class Message:
    """
    A class representing a message.

    Attributes
    ----------
    id_ : str
        The ID of the message.
    type_ : str
        The type of the message.
    date : str
        The date of the message.
    date_unixtime : int
        The UNIX timestamp of the message date.
    from_ : str
        The sender of the message.
    from_id : str
        The ID of the message sender.
    text : str
        The text content of the message.
    text_entities : TextEntity
        The text entities associated with the message.

    Methods
    -------
    __init__(id_, type_, date, date_unixtime, from_, from_id, text, text_entities)
        Initializes a new instance of Message.
    __repr__()
        Returns a string representation of the Message instance.
    __str__()
        Returns a string representation of the Message instance.
    from_dict(data)
        Creates a new Message instance from a dictionary.

    """

    __slots__ = (
        'id_', 'type_', 'date', 'date_unixtime',
        'from_', 'from_id', 'text', 'text_entities'
    )

    def __init__(
        self, id_, type_, date, date_unixtime, from_, from_id, text,
        text_entities: List[TextEntity]
    ):
        """
        Initializes a new instance of the Message class.

        Parameters
        ----------
        id_ : str
            The ID of the message.
        type_ : str
            The type of the message.
        date : str
            The date of the message.
        date_unixtime : int
            The UNIX timestamp of the message date.
        from_ : str
            The sender of the message.
        from_id : str
            The ID of the message sender.
        text : str
            The text content of the message.
        text_entities : TextEntity
            The text entities associated with the message.

        """
        self.id_ = id_
        self.type_ = type_
        self.date = date
        self.date_unixtime = date_unixtime
        self.from_ = from_
        self.from_id = from_id
        self.text = text
        self.text_entities = text_entities

    def __repr__(self):
        """
        Returns a string representation of the Message instance.

        Returns
        -------
        str
            A string representation of the Message instance.

        """
        return (
            f"Message(id_={self.id_}, type_='{self.type_}', date='{self.date}', "
            f"date_unixtime='{self.date_unixtime}', from_='{self.from_}', "
            f"from_id='{self.from_id}', text='{self.text}', "
            f"text_entities={self.text_entities})"
        )

    def __str__(self):
        """
        Returns a string representation of the Message instance.

        Returns
        -------
        str
            A string representation of the Message instance.

        """
        return (
            f"ID: {self.id_}, Type: {self.type_}, Date: {self.date}, From: "
            f"{self.from_}, Text: {self.text}, Text Entities: {self.text_entities}"
        )

    @classmethod
    def from_dict(cls, data):
        """
        Creates a new Message instance from a dictionary.

        Parameters
        ----------
        data : dict
            The dictionary containing message data.

        Returns
        -------
        Message
            A new Message instance.

        """
        text_entities = [TextEntity.from_dict(dte) for dte in data['text_entities']]
        return cls(
            id_=data['id'],
            type_=data['type'],
            date=data['date'],
            date_unixtime=data['date_unixtime'],
            from_=data['from'],
            from_id=data['from_id'],
            text=data['text'],
            text_entities=text_entities
        )


class Chat:
    """
    A class representing a chat.

    Attributes
    ----------
    name : str
        The name of the chat.
    type_ : str
        The type of the chat.
    id_ : str
        The ID of the chat.
    messages : List[Message]
        The list of messages in the chat.

    Methods
    -------
    __init__(name, type_, id_, messages)
        Initializes a new instance of Chat.
    __repr__()
        Returns a string representation of the Chat instance.
    __str__()
        Returns a string representation of the Chat instance.
    from_dict(data)
        Creates a new Chat instance from a dictionary.

    """

    __slots__ = ('name', 'type_', 'id_', 'messages')

    def __init__(self, name, type_, id_, messages: List[Message]):
        """
        Initializes a new instance of the Chat class.

        Parameters
        ----------
        name : str
            The name of the chat.
        type_ : str
            The type of the chat.
        id_ : str
            The ID of the chat.
        messages : List[Message]
            The list of messages in the chat.

        """
        self.name = name
        self.type_ = type_
        self.id_ = id_
        self.messages = messages

    def __repr__(self):
        """
        Returns a string representation of the Chat instance.

        Returns
        -------
        str
            A string representation of the Chat instance.

        """
        return (
            f"Chat(name='{self.name}', type_='{self.type_}', id_={self.id_}, "
            f"messages={self.messages})"
        )

    def __str__(self):
        """
        Returns a string representation of the Chat instance.

        Returns
        -------
        str
            A string representation of the Chat instance.

        """
        return (
            f"Name: {self.name}, Type: {self.type_}, ID: {self.id_}, "
            f"Number of Messages: {len(self.messages)}"
        )

    @classmethod
    def from_dict(cls, data):
        """
        Creates a new Chat instance from a dictionary.

        Parameters
        ----------
        data : dict
            The dictionary containing chat data.

        Returns
        -------
        Chat
            A new Chat instance.

        """
        messages = [Message.from_dict(msg) for msg in data['messages']]
        return cls(
            name=data['name'],
            type_=data['type'],
            id_=data['id'],
            messages=messages
        )
