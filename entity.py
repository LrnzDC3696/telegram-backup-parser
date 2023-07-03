class TextEntities:
    __slots__ = ['type_', 'text']

    def __init__(self, type_, text):
        self.type_ = type_
        self.text = text

    def __repr__(self):
        return f"TextEntities(type_='{self.type_}', text='{self.text}')"

    def __str__(self):
        return f"Type: {self.type_}, Text: {self.text}"

    @classmethod
    def from_dict(cls, data):
        return cls(type_=data['type'], text=data['text'])


class Message:
    __slots__ = [
        'id_', 'type_', 'date', 'date_unixtime',
        'from_', 'from_id', 'text', 'text_entities'
    ]

    def __init__(
        self, id_, type_, date, date_unixtime, from_, from_id, text,
        text_entities: TextEntities
    ):
        self.id_ = id_
        self.type_ = type_
        self.date = date
        self.date_unixtime = date_unixtime
        self.from_ = from_
        self.from_id = from_id
        self.text = text
        self.text_entities = text_entities

    def __repr__(self):
        return (
            f"Message(id_={self.id_}, type_='{self.type_}', date='{self.date}', "
            f"date_unixtime='{self.date_unixtime}', from_='{self.from_}', "
            f"from_id='{self.from_id}', text='{self.text}', "
            f"text_entities={self.text_entities})"
        )

    def __str__(self):
        return (
            f"ID: {self.id_}, Type: {self.type_}, Date: {self.date}, From: "
            f"{self.from_}, Text: {self.text}, Text Entities: {self.text_entities}"
        )

    @classmethod
    def from_dict(cls, data):
        text_entities = TextEntities.from_dict(data['text_entities'][0])
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
    __slots__ = ['name', 'type_', 'id_', 'messages']

    def __init__(self, name, type_, id_, messages: [Message]):
        self.name = name
        self.type_ = type_
        self.id_ = id_
        self.messages = messages

    def __repr__(self):
        return (
            f"Chat(name='{self.name}', type_='{self.type_}', id_={self.id_}, "
            f"messages={self.messages})"
        )

    def __str__(self):
        return (
            f"Name: {self.name}, Type: {self.type_}, ID: {self.id_}, "
            f"Number of Messages: {len(self.messages)}"
        )

    @classmethod
    def from_dict(cls, data):
        messages = [Message.from_dict(msg) for msg in data['messages']]
        return cls(
            name=data['name'],
            type_=data['type'],
            id_=data['id'],
            messages=messages
        )
