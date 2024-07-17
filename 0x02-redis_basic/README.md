# What is Redis
Redis means "Remote Dictionary Server", an in-memory key-value database, it can be used as a cache, data structure store, document database, or vector database.

# Redis Architecture
Redis has a client-server architecture, the `redis-server` can be running on `localhost` or another host, we can connect to the `redis-server` with `redis-cli` or with a client library for any programming language.

## Redis Server
we can `install Redis` based on our OS, or using Docker if we have it, the most important thing we need is how to connect to that server, so we need to know what is the IP of the **host** machine and the **port** Redis server is listening to.

```sh
redis-server
```

this will run the server on `localhost` port `6379`

`redis-server` is highly configurable, we can create a configuration file based on this specifications, and pass it to the `redis-server` if we need, but for now we will stick with the defaults.

## Redis Client
now that we know the host and port of the Redis server we can connect to it with many different clients, lets use redis as a data store
#### Redis CLI
```sh
redis-cli -h 127.0.0.1 -p 6379
# these are the defaults anyway we can just say `redis-cli`
```
this command will connect to the `redis-server` running in `localhost` listening to port `6379`, and after that it opens an interactive shell where we can issue commands to the server.


# Links
[How to Use Redis With Python – Real Python](https://realpython.com/python-redis/)
[Redis configuration | Docs](https://redis.io/docs/latest/operate/oss_and_stack/management/config/)
[Redis as an in-memory data structure store quick start guide](https://redis.io/docs/latest/develop/get-started/data-store/)
[Understand Redis data types | Docs](https://redis.io/docs/latest/develop/data-types/)
