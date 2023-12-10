'''
В реальном использовании не стараются делать синхронизацию этапов в одной целевой задаче с повтором. В действительности стараются делать простую и прозрачную реализацию без лишних усложнений. Вот несколько примеров "боевой" реализации барьера в реальных проектах:

5.  Apache Kafka: барьер используется в Apache Kafka для синхронизации потоков, обрабатывающих сообщения в очереди.
'''

import threading
from kafka import KafkaConsumer, KafkaProducer

class ConsumerThread(threading.Thread):
    def __init__(self, topic, group_id, barrier):
        threading.Thread.__init__(self)
        self.kafka_consumer = KafkaConsumer(topic, group_id=group_id)
        self.barrier = barrier

    def run(self):
        for message in self.kafka_consumer:
            # Обработка сообщения
            self.barrier.wait()

class ProducerThread(threading.Thread):
    def __init__(self, topic, messages, barrier):
        threading.Thread.__init__(self)
        self.kafka_producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        self.topic = topic
        self.messages = messages
        self.barrier = barrier

    def run(self):
        for message in self.messages:
            self.kafka_producer.send(self.topic, message)
            # Ожидание завершения обработки сообщения
            self.barrier.wait()