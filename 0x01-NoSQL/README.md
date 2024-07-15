# Not only SQL for storing data
there will be some situations where your data does not really rely on relation, and you need some flexability with the data store, this is where NoSQL database operate.

# Mongo
Mongo is a document database, where each record of data is represented in a document that looks like a javascript object, that document is stored in collections which is stored in a database.

## `mongosh`
this is a command-line utility to interact with the mongo engine that is running on a host, with it we can admenstrate the engine users, create databases, collections, and doing CRUD operations over documents

```sh
# the following commands do the same thing
# connect to the mongo server running on the local host
mongosh
mongosh mongodb://localhost
mongosh localhost:27017

# Start mongosh using 'ships' database on specified connection string:
mongosh mongodb://192.168.0.5:9999/ships

# execute the scripts inside a .js or .mongodb file inside `mydb` database in the local host
mongosh mydb init.js populate.mongodb
```


### Databases
inside the `mongosh`
to view all databses
```mongosh
show databases
```
