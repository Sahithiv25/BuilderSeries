## Section 2 Redis Architecture

### 4 Important parts
1. Single threaded event loop
2. in-memory storage model
3. persistent options
4. network model and concurrency

### 1. Single threaded event loop
- One thread handles all requests
- No context switching
- No lock contention
- No complicated concurrency issues

### How is it still fast?
- Everything is in RAM (not in disk)
- Operations are O(1)
- Impl is highly optimized C

### 2. In memory storage model
- Data lives in RAM (not disk)
- uses optimised data structures
- RAM access = ~100x faster than disk
- Better to store hot data as it is not ideal for huge datasets

### 3. Persistence
    A. RDB - Snapshotting
        Takes snapshots of db at intervals
        light weight and good for backups
        But,
        may loose writes if Redis crashes
    B. AOF - Append Only File
        Every write operation is appened to a log
        Much safer no data loss
    Best performace = RDB + AOF

### 4. Networking Model
- Non blocking I/O
- Multiplexing
- Even though it is single threaded it handles thousands of concurrent conncetions.

### Command execution is atomic
- No partial writes
- No race conditions
- Ex: INCR page_views: this is atomic operation and no two clients can overlap it

### Questions
1. "Why is Redis single-threaded but fast?"
Because RAM + optimized data structures + no locks.

2. "What happens if Redis crashes?"
RDB uses snapshots → some data lost
AOF logs every operation → minimal loss

3. "Can Redis use multiple cores?"
Yes, but only in special cases:
Redis clusters
I/O threads for networking (Redis 6+)
Replication/sharding
Core logic is still single-threaded.
