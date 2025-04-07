import redis
import time
import random
from datetime import datetime

# Your Upstash Redis credentials
r = redis.Redis(
    host="oriented-feline-60698.upstash.io",
    port=6379,
    password=password,  # truncated for security
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
