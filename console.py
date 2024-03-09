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


class HBNBCommand(cmd.Cmd):
    """Runs HBNB console"""

    prompt = "(hbnb) "

    __available_classes = ('Amenity', 'BaseModel', 'City',
                           'Place', 'Review', 'State', 'User')

    def __get_args(self, line):
        """Gets args from console"""

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
            print("** class name doesn't exist **")
            return False
        elif len(args) == 1:
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
        """Show help for available commands."""
        super().do_help(line)

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """

        args = self.__get_args(line)
        args_are_valid = self.__validate_arguments

        if args_are_valid is False:
            return

        class_name = args[0]

        instance = eval(class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """
        Prints string representateion of instance
        based on the class name and id
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
        Deletes an instance based on the class name and id
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
        Prints all string representation of all instances
        based or not on the class name.
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
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file)
        """

        args = self.__get_args(line)
        args_are_valid = self.__validate_arguments(args)

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
