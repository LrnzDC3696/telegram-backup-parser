__all__ = ("TextEntity", "Message", "Chat")

import os
from typing import List


THUMBNAIL_SUFFIX = "_thumb.jpg"


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

    __slots__ = ("type_", "text")

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
        return cls(type_=data["type"], text=data["text"])


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
        "id_",
        "type_",
        "date",
        "date_unixtime",
        "from_",
        "from_id",
        "text",
        "text_entities",
    )

    def __init__(
        self,
        id_,
        type_,
        date,
        date_unixtime,
        from_,
        from_id,
        text,
        text_entities: List[TextEntity],
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
        text_entities = [TextEntity.from_dict(dte) for dte in data["text_entities"]]
        return cls(
            id_=data["id"],
            type_=data["type"],
            date=data["date"],
            date_unixtime=data["date_unixtime"],
            from_=data["from"],
            from_id=data["from_id"],
            text=data["text"],
            text_entities=text_entities,
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

    __slots__ = ("name", "type_", "id_", "messages")

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
        messages = [Message.from_dict(msg) for msg in data["messages"]]
        return cls(
            name=data["name"], type_=data["type"], id_=data["id"], messages=messages
        )


class File:
    """
    A class representing a file.

    Attributes
    ----------
    file_name : str
        The name of the file.
    file_thumbnail_name : str, optional
        The name of the file's thumbnail (default is None).

    Methods
    -------
    __init__(file_name, file_thumbnail_name=None)
        Initializes a new instance of File.
    from_folder(folder_path)
        Creates a new File instance from a folder path.

    """

    __slots__ = ("file_name", "file_thumbnail_name")

    def __init__(self, file_name, file_thumbnail_name=None):
        """
        Initializes a new instance of the File class.

        Parameters
        ----------
        file_name : str
            The name of the file.
        file_thumbnail_name : str, optional
            The name of the file's thumbnail (default is None).

        """
        self.file_name = file_name
        self.file_thumnail_name = file_thumbnail_name

    def __repr__(self):
        """
        Returns a string representation of the File instance.

        Returns
        -------
        str
            A string representation of the File instance.

        """
        return f"File(name={self.name}, thumbnail_name={self.thumbnail_name})"

    def __str__(self):
        """
        Returns a string representation of the File instance.

        Returns
        -------
        str
            A string representation of the File instance.

        """
        return f"File {self.name}"

    @classmethod
    def from_folder(cls, folder_path):
        """
        Creates a new File instance from a folder path.

        Parameters
        ----------
        folder_path : str
            The path to the folder containing the file.

        Returns
        -------
        list of `File`
            A list of `File` objects.

        """
        files = []

        for file_name in os.listdir(folder_path):
            if os.path.isdir(file_name):
                continue

            file_thumbnail_path = file_name + THUMBNAIL_SUFFIX

            if os.path.isfile(file_thumbnail_path):
                file = cls(file_name, file_thumbnail_path)
            else:
                file = cls(file_name)

            files.append(file)

        return files


class Backup:
    """
    A class representing a backup.

    Attributes
    ----------
    files : List[File]
        The list of files in the backup.
    photos : List[File]
        The list of photos in the backup.
    video_files : List[File]
        The list of video files in the backup.
    voice_messages : List[File]
        The list of voice messages in the backup.
    chat : Chat
        The chat in the backup.

    Methods
    -------
    __init__(files, photos, video_files, voice_messages, chat)
        Initializes a new instance of Backup.
    __repr__()
        Returns a string representation of the Backup instance.
    __str__()
        Returns a string representation of the Backup instance.
    from_folder_path(folder_path)
        Creates a new Backup instance from a folder path.

    """

    __slots__ = ("files", "photos", "video_files", "voice_messages", "chat")
    DIRECTORIES = ("files", "photos", "video_files", "voice_messages")
    CHAT_FILE_NAME = "result.json"

    def __init__(
        self,
        files: List[File],
        photos: List[File],
        video_files: List[File],
        voice_messages: List[File],
        chat: Chat,
    ):
        """
        Initializes a new instance of the Backup class.

        Parameters
        ----------
        files : List[File]
            The list of files in the backup.
        photos : List[File]
            The list of photos in the backup.
        video_files : List[File]
            The list of video files in the backup.
        voice_messages : List[File]
            The list of voice messages in the backup.
        chat : Chat
            The chat in the backup.

        """
        self.files = files
        self.photos = photos
        self.video_files = video_files
        self.voice_messages = voice_messages
        self.chat = chat

    def __repr__(self):
        """
        Returns a string representation of the Backup instance.

        Returns
        -------
        str
            A string representation of the Backup instance.

        """
        return (
            f"Backup(files={self.files}, photos={self.photos}, "
            f"video_files={self.video_files}, voice_messages={self.voice_messages}, "
            f"chat={self.chat})"
        )

    def __str__(self):
        """
        Returns a string representation of the Backup instance.

        Returns
        -------
        str
            A string representation of the Backup instance.

        """
        return (
            f"Backup:\n"
            f"  files: {self.files}\n"
            f"  photos: {self.photos}\n"
            f"  video_files: {self.video_files}\n"
            f"  voice_messages: {self.voice_messages}\n"
            f"  chat: {self.chat}"
        )

    @classmethod
    def from_folder_path(cls, folder_path):
        """
        Creates a new Backup instance from a folder path.

        Parameters
        ----------
        folder_path : str
            The path to the folder containing the backup data.

        Returns
        -------
        Backup
            A new Backup instance.

        """
        files = []
        photos = []
        video_files = []
        voice_messages = []
        chat = None

        for directory in cls.DIRECTORIES:
            files_in_directory = File.from_folder(os.path.join(folder_path, directory))

            if directory == "chat":
                chat = files_in_directory[0]
            else:
                getattr(cls, directory).extend(files_in_directory)

        return cls(files, photos, video_files, voice_messages, chat)
