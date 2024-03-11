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

## Example usage

You'll be using this console to manipulate different objects as named above. You can use the following commands to operate on this objects:

1. create
2. show
3. update
4. destroy
5. all

For example, if you wanted to create a new user, you coulde use this command:

```
create User
```

When you run the `create` command, the id of the created object will be displayed:

```
b419cc1a-e64f-4fde-8556-e021edb08bd2
```

To show this user, run:

```
show User b419cc1a-e64f-4fde-8556-e021edb08bd2
```

This will display this user's details:

```
[User] (b419cc1a-e64f-4fde-8556-e021edb08bd2) {'id': 'b419cc1a-e64f-4fde-8556-e021edb08bd2', 'created_at': datetime.datetime(2024, 3, 11, 0, 32, 18, 862147), 'updated_at': datetime.datetime(2024, 3, 11, 0, 32, 18, 862157)}
```

You could update this user by running:

```
update User b419cc1a-e64f-4fde-8556-e021edb08bd2 name "Brian"
```

Let's see what that looks like now:

```
show User b419cc1a-e64f-4fde-8556-e021edb08bd2
```

This is what we get:

```
[User] (b419cc1a-e64f-4fde-8556-e021edb08bd2) {'id': 'b419cc1a-e64f-4fde-8556-e021edb08bd2', 'created_at': datetime.datetime(2024, 3, 11, 0, 32, 18, 862147), 'updated_at': datetime.datetime(2024, 3, 11, 0, 32, 18, 862157), 'name': 'Brian'}
```

The `update` command only updates one key and value at a time.

Finally, you can destroy this instance using:

```
destroy User b419cc1a-e64f-4fde-8556-e021edb08bd2
```

## Function-like commands

All the object names are actually Python class names. And the commands you've seen above are class methods. Through this console, you can call these methods on instances. For example:

```
User.show("b419cc1a-e64f-4fde-8556-e021edb08bd2")
```

This is the same as running `show User b419cc1a-e64f-4fde-8556-e021edb08bd2`. This is what's printed to stdout:

```
[User] (b419cc1a-e64f-4fde-8556-e021edb08bd2) {'id': 'b419cc1a-e64f-4fde-8556-e021edb08bd2', 'created_at': datetime.datetime(2024, 3, 11, 0, 32, 18, 862147), 'updated_at': datetime.datetime(2024, 3, 11, 0, 32, 18, 862157), 'name': 'Brian'}
```

This syntax will work for all classes. The methods that can be called like this are:

1. update: Example given below.
2. destroy: Give the id as the argument.
3. show: Give the id as the argument.
4. all: Doesn't take any arguments. Will show arguments of the specific class.
5. count: This will give a count of objects of that class. No arguments should be passed.

Example with `<Class_name>.update()`

```
User.update("b419cc1a-e64f-4fde-8556-e021edb08bd2", "<key>", "<value>")
```

`<key>` and `<value>` can be substituted with a dictionary. A dictionary will also enable you to update or add multiple fields. `update` is the only method that takes a dictionary argument.

PS: Use double quotes when passing string arguments to these methods.
