# Realtime Vitals Alert Engine

This project simulates human vitals, detects anomalies, and sends alerts to a Kafka topic.

## Usage

1.  Install Docker.
2.  Build the Docker image: `docker build -t realtime-vitals-alert-engine .`
3.  Run the Docker container, ensuring Kafka is running and accessible.  Set the `KAFKA_TOPIC` and `KAFKA_BOOTSTRAP_SERVERS` environment variables.

    For example:

    ```bash
    docker run -e KAFKA_TOPIC=vitals-topic -e KAFKA_BOOTSTRAP_SERVERS=localhost:9092 realtime-vitals-alert-engine
    ```

## Configuration

*   `KAFKA_TOPIC`:  The Kafka topic to send vitals to (default: `vitals-topic`).
*   `KAFKA_BOOTSTRAP_SERVERS`: The Kafka bootstrap servers (default: `localhost:9092`).