from kafka.admin import * 
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
producer = KafkaProducer(value_serializer = lambda v: json.dumps(v).encode("utf-8"))