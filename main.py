from bs4 import BeautifulSoup
import os
from datetime import datetime


def parse_date_string(date_string):
    format_string = "%d.%m.%Y %H:%M:%S UTC%z"
    return datetime.strptime(date_string, format_string)


class MessageService:
    def __init__(self, id_, body_details):
        self.id_ = id_
        self.body_details = body_details

    def __str__(self):
        return f"Service message {self.id_}: {self.body_details}"

    def __repr__(self):
        return f"MessageService(id_={self.id_}, body_details='{self.body_details}')"

    @classmethod
    def from_bs4(cls, bs4):
        body_details = bs4.find("div", class_="body details").text
        return MessageService(bs4["id"], body_details)


class MessageJoined:
    def __init__(self, id_, body_details):
        self.id_ = id_
        self.body_details = body_details

    @classmethod
    def from_bs4(cls, bs4):
        pass


class Message:
    def __init__(
        self,
        id_,
        initials,
        time_,
        date_,
        from_name,
        reply_to=None,
        text=None,
        media_call_title=None,
        media_call_status=None,
        media_live_location_map_url=None,
        media_live_location_title=None,
        media_live_location_status=None,
        photo_path=None,
        photo_thumb_path=None,
        round_video_message_path=None,
        round_video_message_thumb_path=None,
        round_video_message_title=None,
        round_video_message_status=None,
        video_file_path=None,
        video_file_thumb_path=None,
        video_file_duration=None,
        media_voice_message_path=None,
        media_voice_message_title=None,
        media_voice_message_status=None,
    ):
        # Required
        self.id_ = id_
        self.initials = initials
        self.time_ = time_
        self.date_ = date_
        self.from_name = from_name

        # Not Required
        self.reply_to = reply_to
        self.text = text

        self.media_call_title = media_call_title
        self.media_call_status = media_call_status
        self.media_live_location_map_url = media_live_location_map_url
        self.media_live_location_title = media_live_location_title
        self.media_live_location_status = media_live_location_status
        self.photo_path = photo_path
        self.photo_thumb_path = photo_thumb_path
        self.round_video_message_path = round_video_message_path
        self.round_video_message_thumb_path = round_video_message_thumb_path
        self.round_video_message_title = round_video_message_title
        self.round_video_message_status = round_video_message_status
        self.video_file_path = video_file_path
        self.video_file_thumb_path = video_file_thumb_path
        self.video_file_duration = video_file_duration
        self.media_voice_message_path = media_voice_message_path
        self.media_voice_message_title = media_voice_message_title
        self.media_voice_message_status = media_voice_message_status

    @classmethod
    def from_bs4(cls, bs4):
        _body = bs4.find("div", class_="body")
        _date = _body.find("div", class_="date details")

        # required stuff
        id_ = bs4["id"]
        initials = bs4.find("div", class_="initials")
        time_ = _date.text
        date_ = _date["title"]
        from_name = _date.find("div", class_="from_name").text

        # not required
        reply_to = _body.find("div", class_="reply_to").text
        text = _body.find("div", class_="text").text

        _media_wrap = _body.find("div", class_="media_wrap")

        if _media_wrap is None:
            return cls(id_, initials, time_, date_, from_name)

        # For calls
        _media_call = _media_wrap.find("div", class_="media_call")
        if _media_call is None:
            media_call_title = None
            media_call_status = None

        else:
            media_call_title = _media_call.find("div", class_="title")
            media_call_status = _media_call.find("div", class_="status")

        # For share location
        _media_live_location = _media_wrap.find("a", class_="media_live_location")
        if _media_live_location is None:
            media_live_location_map_url = None
            media_live_location_title = None
            media_live_location_status = None

        else:
            media_live_location_map_url = _media_live_location["href"]
            media_live_location_title = _media_live_location.find("div", class_="title")
            media_live_location_status = _media_live_location.find(
                "div", class_="status"
            )

        # For photos
        _photo_wrap = _media_wrap.find("a", class_="photo_wrap")
        if _photo_wrap is None:
            photo_path = None
            photo_thumb_path = None

        else:
            photo_path = _photo_wrap["href"]
            photo_thumb_path = _photo_wrap.find("img", class_="photo")["src"]

        # For round videos
        _media_video = _media_wrap.find("a", class_="media_video")
        if _media_video is None:
            round_video_message_path = None
            round_video_message_thumb_path = None
            round_video_message_title = None
            round_video_message_status = None

        else:
            round_video_message_path = _media_video["href"]
            round_video_message_thumb_path = _media_video.find("img", class_="thumb")[
                "src"
            ]
            round_video_message_title = _media_video.find("div", class_="title")
            round_video_message_status = _media_video.find("div", class_="status")

        # For video files
        _video_file_wrap = _media_wrap.find("a", class_="video_file_wrap")
        if _video_file_wrap is None:
            video_file_path = None
            video_file_thumb_path = None
            video_file_duration = None

        else:
            video_file_path = _video_file_wrap["href"]
            video_file_thumb_path = _video_file_wrap.find("img", class_="video_file")[
                "src"
            ]
            video_file_duration = _video_file_wrap.find("div", class_="video_duration")

        # For voice messages
        _media_voice_message = _media_wrap.find("a", class_="media_voice_message")
        if _media_voice_message is None:
            media_voice_message_path = None
            media_voice_message_title = None
            media_voice_message_status = None

        else:
            media_voice_message_path = _media_voice_message["href"]
            media_voice_message_title = _media_voice_message.find("div", "title")
            media_voice_message_status = _media_voice_message.find("div", "status")

        return cls(
            id_,
            initials,
            time_,
            date_,
            from_name,
            reply_to=reply_to,
            text=text,
            media_call_title=media_call_title,
            media_call_status=media_call_status,
            media_live_location_map_url=media_live_location_map_url,
            media_live_location_title=media_live_location_title,
            media_live_location_status=media_live_location_status,
            photo_path=photo_path,
            photo_thumb_path=photo_thumb_path,
            round_video_message_path=round_video_message_path,
            round_video_message_thumb_path=round_video_message_thumb_path,
            round_video_message_title=round_video_message_title,
            round_video_message_status=round_video_message_status,
            video_file_path=video_file_path,
            video_file_thumb_path=video_file_thumb_path,
            video_file_duration=video_file_duration,
            media_voice_message_path=media_voice_message_path,
            media_voice_message_title=media_voice_message_title,
            media_voice_message_status=media_voice_message_status,
        )


def find_messages_files(directory):
    message_files = []

    for file_name in os.listdir(directory):
        if not file_name.startswith("message") or not file_name.endswith(".html"):
            continue

        message_files.append(os.path.join(directory, file_name))

    return sorted(message_files)


def parse_messages_service(messages_service):
    body_details = messages_service.find("div", class_="body details")
    return MessageService(messages_service["id"], body_details)


def parse_messages_joined(messages_service):
    pass
    # return MessageJoined(messages_service)


def parse_messages(messages_service):
    pass
    # return Message(messages_service)


if __name__ == "__main__":
    BACKUP_DIRECTORIES = ["ChatExport_2023-02-27", "ChatExport_2023-03-18"]

    # getting all message file
    message_files_paths = []
    for dir_ in BACKUP_DIRECTORIES:
        message_files_paths.extend(find_messages_files(dir_))

    message_all = []
    message_service_list = []
    message_joined_list = []
    message_list = []

    for message_file_path in message_files_paths:
        with open(message_file_path) as message_file:
            zoup = BeautifulSoup(message_file, "lxml")

        for child in zoup.find_all("div", class_="message"):
            child_class = child["class"]

            # check what kind of child
            if "service" in child_class:
                parsed_message = parse_messages_service(child)
                message_all.append(parsed_message)
                message_service_list.append(parsed_message)

            elif "joined" in child_class:
                parsed_message = parse_messages_joined(child)
                # message_all.append(parsed_message)
                # message_joined_list.append(parsed_message)

            else:
                parsed_message = parse_messages(child)
                # message_all.append(parsed_message)
                # message_list.append(parsed_message)

    # print the output
    for message in message_all:
        print(message)
