from google.cloud import pubsub_v1
import time

# Initialize Subscriber client
project_id = "golden-plateau-434303-r2"
subscription_id = "receive_data-sub"

# Create a Subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Full path to the subscription
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Callback function to handle messages
def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    
    # Acknowledge the message
    message.ack()
    print("Message acknowledged.")

# Subscribe to the subscription
def listen_for_messages():
    """Subscribe to the Pub/Sub subscription and listen for messages."""
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...\n")

    # Keep the listener active
    with subscriber:
        try:
            # Block indefinitely while waiting for messages
            streaming_pull_future.result()
        except KeyboardInterrupt:
            streaming_pull_future.cancel()
            streaming_pull_future.result()

if __name__ == "__main__":
    listen_for_messages()