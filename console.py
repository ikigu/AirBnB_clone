#!/usr/bin/python3
"""Defines the HBNBCommand class for command line interpretation."""

from models.base_model import BaseModel
from models.user import User
from models import storage

import cmd


class HBNBCommand(cmd.Cmd):
    """Runs HBNB console"""

    prompt = "(hbnb) "
    intro = "Welcome to the hbnb command interpreter type 'help' to list available commands"

    __available_classes = ('BaseModel', 'User')

    def __validate_arguments(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif arg.split()[0] not in HBNBCommand.__available_classes:
            print("** class name doesn't exist **")
            return False
        elif len(arg.split()) == 1:
            print("** instance id missing **")
            return False

    def do_quit(self, arg):
        """Quit the command interpreter."""
        exit()

    do_EOF = do_quit

    def emptyline(self):
        """Handle an empty line input."""
        pass

    def do_help(self, arg):
        """Show help for available commands."""
        super().do_help(arg)

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Args:
            self: represents object instance
            arg (string): space-delimited list of arguments
        """

        if len(arg) == 0:
            return print("** class name missing **")
        elif arg not in HBNBCommand.__available_classes:
            return print("** class doesn't exist **")

        instance = eval(arg)()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """
        Prints stirng representateion of instance
        based on the class name and id

        Args:
            self: represents object instance
            arg: space-delimited list of arguments
        """

        args_are_valid = self.__validate_arguments(arg)

        if args_are_valid is False:
            return

        all_objects = storage.all()

        try:
            instance = all_objects[f"{arg.split()[0]}.{arg.split()[1]}"]
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Args:
            self: represents object instance
            args: space-delimited list of arguments
        """

        args_are_valid = self.__validate_arguments(arg)

        if args_are_valid is False:
            return

        all_objects = storage.all()

        try:
            del all_objects[f"{arg.split()[0]}.{arg.split()[1]}"]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Args:
            self: represents object instances
            arg: space-delimited list of arguments
        """

        all_objects = storage.all()

        if len(arg) == 0:
            return print(all_objects)

        class_name = arg.split()[0]

        if class_name in self.__available_classes:
            return print([v.__str__() for k, v in all_objects.items() if class_name in k])
        else:
            return print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into
        the JSON file)

        Args:
            self: object instance
            arg: space-delimited arguments
        """

        args_are_valid = self.__validate_arguments(arg)

        if args_are_valid is False:
            return

        try:
            attr_key = arg.split()[2]
        except IndexError:
            return print("** attribute name missing **")

        try:
            attr_value = arg.split()[3]
        except IndexError:
            return print("** value missing **")

        try:
            attr_value = int(attr_value)
        except ValueError:
            pass

        all_objects = storage.all()
        class_name = arg.split()[0]
        instance_id = arg.split()[1]

        try:
            target_instance = all_objects[f"{class_name}.{instance_id}"]
            target_instance.__dict__[attr_key] = attr_value
            storage.save()
        except KeyError:
            print("** no instance found **")

        # ToDo: Accept multi-word args surrounded by quotes


if __name__ == '__main__':
    HBNBCommand().cmdloop()
