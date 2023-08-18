import os
import json
import vampytest

BACKUP_PATH = os.path.join("backups", "ChatExport_2023-06-28")
RESULT_FILE_PATH = os.path.join(BACKUP_PATH, "result.json")

ACTION_FIELDS_TO_REMOVE = ("actor", "actor_id", "action", "text", "text_entities")
OPTIONAL_ACTION_FIELDS_TO_REMOVE = (
    "emoticon",
    "type",
    "date",
    "date_unixtime",
    "id",
    "duration_seconds",
    "discard_reason",
    "message_id",
)

MSG_FIELDS_TO_REMOVE = (
    "id",
    "type",
    "date",
    "date_unixtime",
    "from",
    "from_id",
    "text",
)

OPTIONAL_MSG_FIELDS_TO_REMOVE = (
    "photo",
    "width",
    "height",
    "reply_to_message_id",
    "edited",
    "edited_unixtime",
    "file",
    "mime_type",
    "duration_seconds",
    "media_type",
    "thumbnail",
)


def yeet_fields(obj, fields):
    for field in fields:
        obj.pop(field)

    return obj


def yeet_optional_fields(obj, fields):
    for field in fields:
        if obj.get(field):
            obj.pop(field)

    return obj


def filter_empty(iterable):  # Can't think of a better name, please suggest
    return [n for n in iterable if n]


def test_dummy_data_result():
    with open(RESULT_FILE_PATH, "r") as json_file:
        # Load the JSON data into a Python dictionary
        json_data = json.load(json_file)

    json_data.pop("name")
    json_data.pop("type")
    json_data.pop("id")
    messages = json_data.pop("messages")

    vampytest.assert_eq(json_data, {})
    types_of_message = set()

    # Testing Messages
    for message in messages:
        types_of_message.add(message["type"])
        if message.get("type") == "service":
            message = yeet_fields(message, ACTION_FIELDS_TO_REMOVE)
            message = yeet_optional_fields(message, OPTIONAL_ACTION_FIELDS_TO_REMOVE)

            vampytest.assert_eq(message, {})
            continue

        message = yeet_fields(message, MSG_FIELDS_TO_REMOVE)
        message = yeet_optional_fields(message, OPTIONAL_MSG_FIELDS_TO_REMOVE)

        text_entities = message.pop("text_entities")
        for text_entity in text_entities:
            text_entity.pop("type")
            text_entity.pop("text")

        vampytest.assert_eq(text_entity, {})
        vampytest.assert_eq(message, {})

    vampytest.assert_eq(filter_empty(text_entities), [])
    vampytest.assert_eq(filter_empty(messages), [])
    print("===="*5)
    print(f"message types: {types_of_message}")
    print("===="*5)
