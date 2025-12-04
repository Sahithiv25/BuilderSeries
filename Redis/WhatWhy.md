# Redis

## Section 1 What is Reddis and Why it Exists
### Redis is an in-memory, key-value data store
### Used for ultra fast operations like Caching, Sessions, queues, rate limiting and real-time analytics.
### In-memory -> everything is stored in RAM
### Single threaded but extremely optimized
### Usecase: as cache, database and message broker

### Why it exists: 
### -- Dbs are fast but still too slow for certain workload
### -- Causes slow reads, expensive resources, high latency
### -- Redis solves this problem
###     --- Faster r/w
###     --- Atomic ops
###     --- Low operational cost
###     --- Very high throughput

### Best usecase: Cache slow db queries, store user session tokens, rate limiting APIs, Pub/Sub for notifications, real time counters (likes/views)