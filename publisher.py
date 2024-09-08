from google.cloud import pubsub_v1
import json
import time

# Initialize Publisher client
project_id = "golden-plateau-434303-r2"
topic_id = "receive_data"

# Create a Publisher client
publisher = pubsub_v1.PublisherClient()

# Full path to the topic
topic_path = publisher.topic_path(project_id, topic_id)

# Function to publish a message
def publish_message(data):
    """Publish a message to the Pub/Sub topic."""
    # Data must be a bytestring
    data = data.encode("utf-8")
    # Publish data to the topic
    future = publisher.publish(topic_path, data)
    print(f"Published message ID: {future.result()}")

# Create dummy messages
def generate_dummy_messages():
    """Generate dummy messages as JSON."""
    for i in range(10):
        message = {
            "message_id": i,
            "content": f"Dummy message {i}",
            "timestamp": time.time()
        }
        # Publish the message as JSON string
        publish_message(json.dumps(message))
        time.sleep(1)  # Adding delay for demo purposes

if __name__ == "__main__":
    generate_dummy_messages()
