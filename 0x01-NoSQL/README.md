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
inside the `mongosh` shell


to view all databses:
```mongosh
show databases;
```

to create a database:
```mongosh
use dbName;
```
This will create the data base but if we didn't add anything to that database it will not be there after closing the `mongosh`, we need to create at least a collection


Create a document:
```js
db.school.insertOne({ name: "Holberton School" });
```
Dont worry I know we didn't create a `school` collection but this command will create the collection if it does not exists.


Retrieve documents:
```js
// find all documens
db.school.find()

// find documents with a specific attribute and value
db.school.find({ name: 'Holberton school' });
```


Update documents:
```js
db.collection.updateMany({ /* matchers */ }, {
    $set: { key: 'value' },
    $unset: ['useless', 'attributes'],
}, {/* Options (upsert: true) */})
// there is db.collection.updateOne also
```


Delete documents:
```js
db.collection.deleteMany({ /* matchers */ })
db.collection.deleteOne({ /* matchers */ })
```

this is all the CRUD with mongosh


## Resources to learn more
[CRUD Operations - MongoDB Manual](https://www.mongodb.com/docs/manual/crud/#std-label-crud)
