from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

df = pd.read_csv("healthcare.csv")

for index, row in df.iterrows():
    data = row.to_dict()
    producer.send('healthstream', value=data)
    print("Sent:", data)
    time.sleep(2)

producer.flush()