# Airbnb Clone - The console

The first step in creating this AirBnB clone is setting up a storage engine for the data needed by the app. The engine includes a command interpreter to manage app objects. The command interpreter can be used to run CRUD and other operations (counting, computing stats, etc) on app objects.

## Running the command interpreter

To start the command interpreter, first clone this repository by running this command on your terminal:

```bash
git clone https://github.com/ikigu/AirBnB_clone
```

Then `cd` into the `AirBnB_clone` repository:

```bash
cd AirBnB_clone
```

Finally, launch the console by running:

```bash
./console.py
```

## Available commands

When the console starts, a prompt will be shown:

```
(hbnb)
```

To list all available commands, run:

```
(hbnb) help
```

This will list out all the commands that can be run on the console. To learn the syntax and function of each command, you can run:

```
(hbnb) help <command>
```

## Available Objects

This console allows you to operate on the following objects:

1. Amenity
2. BaseModel
3. City
4. Place
5. Review
6. State
7. User
