from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: x.encode('utf-8')
)

print("Type messages to send to Kafka (type 'exit' to quit):")
while True:
    try:
        message = input("Your message: ")
        if message.lower() == 'exit':
            break
        producer.send('construction-site', value=message)
        print("Sent!")
    except KeyboardInterrupt:
        break

producer.close()
print("\nProducer closed")