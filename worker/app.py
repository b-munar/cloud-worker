import os
from config import Config

from google.cloud import pubsub_v1

from utils.compress import compress_zip

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/usr/src/app/linen-mason-384315-d051f5f132d3.json'

subscriber = pubsub_v1.SubscriberClient()

subscription_path = subscriber.subscription_path(Config.GOOGLE_CLOUD_PROJECT, "compress-sub")


def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received {message.data!r}.")
    if int(message.attributes['type_task']) == 1:
        compress_zip(int(message.attributes['file_id']))
    message.ack()


streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")


with subscriber:
    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()

        
