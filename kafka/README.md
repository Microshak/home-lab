# Study Guide for Confluent's Apache Kafka Administrator Exam

This guide will go through the Kafka broker settings that are represented in [this quizlet.](https://quizlet.com/609640258/confluent-certified-developer-certification-flash-cards/) The included `docker-compose.yaml` stands up a single Zookeeper node and Kafka broker for testing.

Additionally, the included dockerfile should contain all necessary tools to make your learning easier when entering the container and navigating the environment the Kafka broker runs in.

To start, run:

```sh
docker-compose up --build -d
```

## Single broker
* [Server Settings](./ServerSettings.md)
* [Kafka CLI](./CLI.md)
* [C# Producer/Consumer](./DotNet.md)

To bring down the containers run:
```
docker-compose down
```

## multiple Broker
To start, run 
```

docker-compose  -f docker-compose-multiple.yaml up --build -d

```

