#!/usr/bin/python3
"""
This module defines the HBNBCommand class for the command interpreter.
"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        Empty line + Enter shouldn't execute anything
        """
        pass

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print the id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if (
            class_name not in globals()
            or not issubclass(globals()[class_name], BaseModel)
           ):
            print("** class doesn't exist **")
            return
        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if (
            class_name not in globals() or not
            issubclass(globals()[class_name], BaseModel)
           ):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if (
            class_name not in globals() or not
            issubclass(globals()[class_name], BaseModel)
           ):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = arg.split()
        obj_list = []
        if len(args) == 0:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
            return
        class_name = args[0]
        if (
            class_name not in globals() or not
            issubclass(globals()[class_name], BaseModel)
           ):
            print("** class doesn't exist **")
            return
        for key, value in storage.all().items():
            if class_name in key:
                obj_list.append(str(value))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if (
            class_name not in globals() or not
            issubclass(globals()[class_name], BaseModel)
           ):
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + "." + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        instance = storage.all()[key]
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
