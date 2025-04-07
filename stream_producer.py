import redis
import time
import random
from datetime import datetime

r = redis.Redis(
    host='your-upstash-host.upstash.io',
    port=6379,
    password='your-password',
    ssl=True,
    decode_responses=True
)

def generate_events():
    event_types = ['login', 'logout', 'click', 'purchase']
    for _ in range(10):
        event = {
            'event_type': random.choice(event_types),
            'user_id': str(random.randint(1000, 9999)),
            'timestamp': datetime.now().isoformat()
        }
        r.xadd('user_events', event)
        print(f"Published: {event}")
        time.sleep(1)

generate_events()
