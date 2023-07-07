import os
import json
import vampytest

BACKUP_PATH = os.path.join("backups", "ChatExport_2023-06-28")
RESULT_FILE_PATH = os.path.join(BACKUP_PATH, "result.json")

# Can't think of a better name, please suggest


def filter_empty(iterable):
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

    # Testing Messages
    for message in messages:
        if message.get("actor"):
            message.pop("actor")
            message.pop("actor_id")
            message.pop("action")
            message.pop("text")
            message.pop("text_entities")

            if message.get("emoticon"):
                message.pop("emoticon")

            if message.get("type"):
                message.pop("type")

            if message.get("date"):
                message.pop("date")

            if message.get("date_unixtime"):
                message.pop("date_unixtime")

            if message.get("id"):
                message.pop("id")

            if message.get("duration_seconds"):
                message.pop("duration_seconds")

            if message.get("discard_reason"):
                message.pop("discard_reason")

            if message.get("message_id"):
                message.pop("message_id")

            continue

        message.pop("id")
        message.pop("type")
        message.pop("date")
        message.pop("date_unixtime")
        message.pop("from")
        message.pop("from_id")
        message.pop("text")

        text_entities = message.pop("text_entities")

        # new optional stuff
        if message.get("photo"):
            message.pop("photo")
            message.pop("width")
            message.pop("height")

        if message.get("reply_to_message_id"):
            message.pop("reply_to_message_id")

        if message.get("edited"):
            message.pop("edited")
            message.pop("edited_unixtime")

        if message.get("file"):
            message.pop("file")
            message.pop("mime_type")

            if message.get("duration_seconds"):
                message.pop("duration_seconds")

            if message.get("media_type"):
                message.pop("media_type")

            if message.get("thumbnail"):
                message.pop("thumbnail")

            if message.get("width"):
                message.pop("width")

            if message.get("height"):
                message.pop("height")

        for text_entity in text_entities:
            text_entity.pop("type")
            text_entity.pop("text")

            vampytest.assert_eq(text_entity, {})
        vampytest.assert_eq(message, {})

    vampytest.assert_eq(filter_empty(text_entities), [])
    vampytest.assert_eq(filter_empty(messages), [])
