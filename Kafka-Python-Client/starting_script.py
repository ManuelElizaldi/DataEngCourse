from kafka.admin import * 
from kafka.admin import KafkaProducer
import json

# define the kafkaadminclient object
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

# to create a topic, first we define an empty list 
topic_list = []

# then you create the new topic class with name, partition and replication factors 
new_topic = NewTopic(name = "bankbranch", num_partitions = 2, replication_factors = 2)
topic_list.append(new_topic)

# you can use this to create topics:
# this is equal to the kafka cli command => kafka-topics.sh --topic
admin_client.create_topics(new_topics = topic_list)

# describing a topic
configs = admin_client.describe_configs(config_resources = [ConfigResource(ConfigResourceType.TOPIC, "bankbranch")])

# kafka producer
# the producer creates messages
# most of the messages are in json format

# defining a producer
# Since Kafka produces and consumes messages in raw bytes, you need to encode our JSON messages and serialize them into bytes. For the value_serializer argument, you will define a lambda function to take a Python dict/list object and serialize it into bytes.
producer = KafkaProducer(value_serializer = lambda v: json.dumps(v).encode("utf-8"))

# now with the producer defined you can start sending messages:
# the first argument defines the topic used, the second argument defines the key value pair message which will be serialized using a lambda function
producer.send("bankbranch", {'atmid':1, 'transid':100})
producer.send("bankbranch", {'atmid':2, 'transid':101})


# kafka consumer
# defining a kafka consumer and subscribing it to the topic bankbranch
consumer = KafkaConsumer("bankbranch")

# you can iterate and print the messages:
for msg in consumer:
    # we do decode because we need to encode the messages into bytes when sending data to kafka
    print(msg.value.decode("utf-8"))