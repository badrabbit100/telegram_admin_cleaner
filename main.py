from telethon import TelegramClient, sync
import time
import settings


client = TelegramClient(settings.session_id, settings.api_id, settings.api_hash)
client.start()


def clean_messages(channel_name: str, limit_messages: int, update_time: int) -> None:
    """
    :param channel_name: string name of channel to delete service messages
    :param limit_messages: define limit of last messages to check from channel
    :param update_time: define checking time in seconds between each checking iteration
    :return: None
    """
    while True:
        messages = (client.get_messages(channel_name, limit=limit_messages))
        for message in messages:
            if message.message is None:
                client.delete_messages(channel_name, message.id)
        time.sleep(update_time)


def main():
    """ Start main program messages"""
    clean_messages(
        channel_name=settings.channel_name,
        limit_messages=settings.limit_messages_to_clean,
        update_time=1
    )


if __name__ == '__main__':
    main()

