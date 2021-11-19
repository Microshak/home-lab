import requests
from kafka import KafkaProducer
import json

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()

ret = {}
ret["coin"] = "222"
ret["time"] = data["time"]["updatedISO"]
ret["rate"] = data["bpi"]["USD"]["rate"]

print(ret)
producer = KafkaProducer(bootstrap_servers='micros:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('fat', ret)

#for _ in range(100):
#     producer.send('foobar', b'some_message_bytes')



producer.send('coin',ret)
#producer2 = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
#producer2.send('fizzbuzz', {'foo': 'bar'})