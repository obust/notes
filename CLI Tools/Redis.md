# Redis

Redis is an open source, **in-memory data structure store**, used as database, cache and message broker. It supports data structures such as [strings](http://redis.io/topics/data-types-intro#strings), [hashes](http://redis.io/topics/data-types-intro#hashes), [lists](http://redis.io/topics/data-types-intro#lists), [sets](http://redis.io/topics/data-types-intro#sets), [sorted sets](http://redis.io/topics/data-types-intro#sorted-sets) with range queries, [bitmaps](http://redis.io/topics/data-types-intro#bitmaps), [hyperloglogs](http://redis.io/topics/data-types-intro#hyperloglogs) and [geospatial indexes](http://redis.io/commands/geoadd) with radius queries.

Redis is what is called a **key-value store** (often referred to as a NoSQL database). The essence of a key-value store is the ability to store some data, called a value, inside a key. This data can later be retrieved only if we know the exact key used to store it.

You can run atomic operations on these types, like:
- appending to a string;
- incrementing the value in a hash;
- pushing an element to a list;
- computing set intersection, union and difference;
- getting the member with highest ranking in a sorted set.  

In order to achieve its outstanding performance, Redis works with an **in-memory dataset**. Depending on your use case, you can persist it either by dumping the dataset to disk every once in a while, or by appending each command to a log. Persistence can be optionally disabled, if you just need a feature-rich, networked, in-memory cache.  

Redis also supports trivial-to-setup master-slave asynchronous replication, with very fast non-blocking first synchronization, auto-reconnection with partial resynchronization on net split.

## Interactive Tutorial

http://try.redis.io/

## Installation

Ubuntu 16.04  
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04


## Connect to Database


**Start client** (default database is number 0 out of 16)  
`redis-cli`

**Change database**  
`SELECT <db-number>`

**List all keys in database**
`KEYS *`

**Stop client**  
`QUIT`


## CLI

**Set value**  
`SET <key> <value>`

**Set value, if the key does not exist**  
`SETNX <key> <value>`

**Get value**  
`GET <key>`

**Delete a key-value pair**  
`DEL <key>`

**Increment a value stored at a key**  
`INCR <key>`

**Set key-value expiration time**  
`EXPIRE <key> <seconds>`

**Get key-value expiration time left**  
`TTL <key>`
- `-2`: key does not exist (anymore)
- `-1`: key will not expire
- `<int>`: key will expire in <int> seconds

## Data Structures

http://redis.io/topics/data-types-intro

### String

A Redis [string]() type is the simplest type of value.


### List

A [list](http://redis.io/topics/data-types-intro#lists) is a **sequence of ordered values**.

ACTION                       | COMMAND [(all)](http://redis.io/commands#list)
-----------------------------|--------------------------------------------
Append list                  | `RPUSH <list-key> <value>`
Prepend list                 | `LPUSH <list-key> <value>`
Get element of list by index | `LINDEX <list-key> <index>`
Get subset of list           | `LRANGE <list-key> <from-index> <to-index>`
Get length of list           | `LLEN <list-key>`
Remove and get first element | `LPOP <list-key>`
Remove and get last element  | `RPOP <list-key>`
Remove occurrences of an element by value  | `LREM <list-key> <count> <value>`

### Set

A [set](http://redis.io/topics/data-types-intro#sorted-sets) is an **unordered collection of values**.  

ACTION                                 | COMMAND [(all)](http://redis.io/commands#set)
---------------------------------------|--------------------------------------
List all values in set                 | `SMEMBERS <set-key>`
Add value to set                       | `SADD <set-key> <value>`
Remove value from set                  | `SREM <set-key> <value>`
Check if value is in set               | `SISMEMBER <set-key> <value>` (`1`: True, `0`: False)
Combine sets (and return all elements) | `SUNION <set-key1> <set-key2> [<set-key3>]`

### Sorted Sets

A [sorted set](http://redis.io/topics/data-types-intro#sets) is an **ordered collection of strings**.

ACTION                       | COMMAND [(all)](http://redis.io/commands#soreted_set)
-----------------------------|--------------------------------------
Add value to sorted set      | `ZADD <set-key> <rank> <value>`
Get subset of sorted set     | `ZRANGE <set-key> <from-index> <to-index>`

### Hash

A [hash](http://redis.io/topics/data-types-intro#hashes) is a **mapping between string fields and values**.

They are used to represent objects (e.g. A User with fields: name, surname, age, etc).

ACTION                             | COMMAND [(all)](http://redis.io/commands#hash)
-----------------------------------|-------------------------------------------
Set hash field                     | `HSET <hash-key> <field> <value>`
Set multiple hash field            | `HMSET <hash-key> <field1> <value1> <field2> <value2>`
Get hash field value               | `HGET <hash-key> <field>`
Get all hash field values          | `HGETALL <hash-key>`
Increment hash field integer value | `HINCRBY <hash-key> <field> <increment>`
Delete hash field(s)               | `HDEL <hash-key> <field> [<field2>]`
