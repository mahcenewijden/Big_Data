from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'construction-site',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='latest'  # Changed from 'earliest' to 'latest'
)
try:
    print("Consumer ready! Waiting for messages...")
    for message in consumer:
        print(f"\nNew message: {message.value.decode('utf-8')}")
except KeyboardInterrupt:
    print("\nConsumer stopped")
finally:
    consumer.close()