#!/usr/bin/python3
"""Defines the HBNBCommand class for command line interpretation."""

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

import cmd


class_lookup = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class HBNBCommand(cmd.Cmd):
    """Runs HBNB console"""

    prompt = "(hbnb) "

    __available_classes = ('Amenity', 'BaseModel', 'City',
                           'Place', 'Review', 'State', 'User')

    def __get_args(self, line):
        """
        Gets args from console and creates a list.
        Multiword arguments surrounded by double quotes
        are treated as a single argument.
        """

        if '"' not in line:
            return line.split()

        open_quote = False
        arguments_list = []
        current_argument = ""

        # Loop through the string
        for char in line:
            if open_quote is False and char == '"':
                open_quote = True
                continue
            elif open_quote is True and char == '"':
                open_quote = False
                arguments_list.append(current_argument)
                current_argument = ""
            elif open_quote is True and char == ' ':
                current_argument += char
            elif open_quote is False and char == ' ':
                if len(current_argument) != 0:
                    arguments_list.append(current_argument)
                    current_argument = ""
            elif char not in ' "':
                current_argument += char

        if current_argument:
            arguments_list.append(current_argument)

        return arguments_list

    def __validate_arguments(self, args, command=None):
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__available_classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1 and command != 'create':
            print("** instance id missing **")
            return False
        elif command == 'update' and len(args) == 2:
            print("** attribute name missing **")
            return False
        elif command == 'update' and len(args) == 3:
            print("** value missing **")
            return False

    def do_quit(self, line):
        """Quit the command interpreter."""
        exit()

    do_EOF = do_quit

    def emptyline(self):
        """Handle an empty line input."""
        pass

    def do_help(self, line):
        """
        Shows all available commands. Run:

            help <command>

        to show help for a specific command.

        Synopsis:
            help <optional command>
        """
        super().do_help(line)

    def do_create(self, line):
        """
        Creates a new instance of an object,
        saves it to storage and prints the id of the new object.

        Synopsis:
            create <Object>

        Availabe Object names:
            1. Amenity
            2. BaseModel
            3. City
            4. Place
            5. Review
            6. State
            7. User
        """

        args = self.__get_args(line)
        args_are_valid = self.__validate_arguments(args, 'create')

        if args_are_valid is False:
            return

        class_name = args[0]

        instance = eval(class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        Prints string representateion of instance
        based on the Object name and id.

        Synopsis:
            show <Object> <Object_id>

        Availabe Object names:
            1. Amenity
            2. BaseModel
            3. City
            4. Place
            5. Review
            6. State
            7. User
        """

        args = self.__get_args(line)
        args_are_valid = self.__validate_arguments(args)

        if args_are_valid is False:
            return

        all_objects = storage.all()

        class_name = args[0]
        object_id = args[1]

        try:
            instance = all_objects[f"{class_name}.{object_id}"]
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the Object name and id.

        Synopsis:
            destroy <Object> <Object_id>

        Availabe Object names:
            1. Amenity
            2. BaseModel
            3. City
            4. Place
            5. Review
            6. State
            7. User
        """

        args = self.__get_args(line)
        args_are_valid = self.__validate_arguments(args)

        if args_are_valid is False:
            return

        all_objects = storage.all()
        class_name = args[0]
        object_id = args[1]

        try:
            del all_objects[f"{class_name}.{object_id}"]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints the string representation of all Objects.
        To show objects of a single type, run:

            all <Object>

        Synopsis:
            all <optional Object name>

        Available Objects:
            1. Amenity
            2. BaseModel
            3. City
            4. Place
            5. Review
            6. State
            7. User
        """

        all_objects = storage.all()

        if len(line) == 0:
            return print([v.__str__() for k, v in all_objects.items()])

        class_name = line.split()[0]

        if class_name in self.__available_classes:
            return print([v.__str__()
                          for k, v in all_objects.items() if class_name in k])
        else:
            return print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an Object based on the Object name and id.
        This command can also be used to add a new attribute,
        with no differences in use.

        Synopsis:
            update <Object> <Object_id> <attribute_key> <attribute_value>

        Availabe Object names:
            1. Amenity
            2. BaseModel
            3. City
            4. Place
            5. Review
            6. State
            7. User
        """

        args = self.__get_args(line)
        args_are_valid = self.__validate_arguments(args, 'update')

        if args_are_valid is False:
            return

        class_name = args[0]
        object_id = args[1]
        attr_key = args[2]
        attr_value = args[3]

        try:
            attr_value = int(attr_value)
        except ValueError:
            pass

        all_objects = storage.all()

        try:
            target_instance = all_objects[f"{class_name}.{object_id}"]
            target_instance.__dict__[attr_key] = attr_value
            storage.save()
        except KeyError:
            print("** no instance found **")

    def __get_method_arguments(self, line):
        """
        Retrieves the arguments passed to a method,
        when a command given to the console is a function.
        """

        arguments_string = []

        if '}' in line:
            arguments_string = line[:-1].split(',', 1)
        else:
            arguments_string = line[:-1].split(',')

        parsed_arguments = []

        for word in arguments_string:
            word = word.strip()

            if word[-1] == '"':
                word = word.replace('"', '')

            if word[-1] == '}':
                word = eval(word)

            if "." in word and type(word) == str:
                print(word)
                try:
                    word = float(word)
                except ValueError:
                    pass
            elif type(word) is str:
                try:
                    word = int(word)
                except ValueError:
                    pass

            parsed_arguments.append(word)

        return tuple(word for word in parsed_arguments)

    def default(self, line):
        try:
            parts = line.split('.', 1)
            class_ = class_lookup.get(parts[0])

            if class_ is None:
                return print("** class doesn't exist **")

            method_and_arguments_list = parts[1].split('(')
            method_name = method_and_arguments_list[0]
            arguments = method_and_arguments_list[1]

            args = []
            kwargs = {}

            if (arguments == ')'):
                arguments = tuple()
            else:
                arguments = self.__get_method_arguments(arguments)

                for arg in arguments:
                    if type(arg) == str:
                        args.append(arg)
                    elif type(arg) == dict:
                        for k, v in arg.items():
                            kwargs[k] = v

                args = tuple(a for a in args)

            result = getattr(class_, method_name)(*args, **kwargs)

        except (IndexError, KeyError, AttributeError, TypeError) as e:
            print(e)
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
