from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError
from typing import Optional, List

config = {
    "bootstrap_servers": ["localhost:9092"],
    "client_id": "admin",
    "topic_name": ["first_t"],
}


class BrokerClient:
    def __init__(self, **kwargs) -> None:
        self.admin = KafkaAdminClient(
            bootstrap_servers=kwargs["bootstrap_servers"],
            client_id=kwargs["client_id"]
        )
        self._create_topics(kwargs["topic_name"])

    def _create_topics(self, topic_names: Optional[str, List[str]], num_partitions: int = 1) -> None:
        topics = []

        if isinstance(topic_names, List):
            pass
        else:
            topic_names = [topic_names]

        for topic_name in topic_names:
            try:
                topics.append(NewTopic(
                    name=topic_name,
                    num_partitions=num_partitions,
                    replication_factor=1
                ))
                self.admin.create_topics(topics)
            except TopicAlreadyExistsError:
                pass