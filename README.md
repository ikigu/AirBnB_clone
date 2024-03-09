# Airbnb Clone - The console

This repository sets up a storage engine for the data needed by the HBNB app. It creates the following models:

-   Base Model
-   User Model
-   City Model
-   Amenity Model
-   Place Model
-   Review Model
-   State Model

## The console

A console is included to run CRUD operations on the file storage system. To interact run:

```
<command> <Model> <object_id>
```

The following commands are available

1. `show`: requires a model and the object id: Shows string representation of an object.
2. `all`: <Model> is optional. Will show all objects in your storage. When <Model> is added, will show objects of that model.
3. `destroy`: add <Model> and <object_id> to destroy a particular object
4. `update`: add <Model> and <object_id>, followed by <attribute_key> <attrribute_value> to update an object of a particular id. Only one key/value pair can be updated at a time.
5. `create`: Takes one argument, <Model> and creates an object of that type. Returns the id of the new object.

## Running the console

1. First clone the repo by running:

```bash
git clone https://github.com/ikigu/AirBnB_clone
```

2. Then cd into the AirBnB directory

```bash
cd AirBnB_clone
```

3. Finally, launch the console by running the following command:

```bash
./console.py
```
