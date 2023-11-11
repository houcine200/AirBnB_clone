#!/usr/bin/python3
"""
Console Module
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb)"

    class_names = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review, }

    def do_quit(self, arg):
        """
        Quit the command-line interpreter.
        """
        return True

    def do_EOF(self, arg):
        """
        Handle End-of-File condition.
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of a specified class.

        Prints the ID of the newly created instance.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.class_names:
            print("** class doesn't exist **")
        else:
            new_instance = self.class_names[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.

        Prints the string representation of the instance.
        """
        if not arg:
            print("** class name missing **")
        args = arg.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
        if len(args) <= 1:
            print("** instance id missing **")
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            instance = storage.all()[key]
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy an instance by removing it from the storage.

        Removes the instance from the storage.
        """
        if not arg:
            print("** class name missing **")
        args = arg.split()
        if args[0] not in self.class_names:
            print("** class doesn't exist **")
        if len(args) <= 1:
            print("** instance id missing **")
        class_name = args[0]
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Display all instances or instances of a specified class.

        Prints the string representation of instances.
        """
        if not arg:
            all_instances = storage.all().values()
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in self.class_names:
                print("** class doesn't exist **")
                return
            all_instances = [
                instance for key, instance in storage.all().items()
                if key.split(".")[0] == class_name
                  ]

            print([str(instance) for instance in all_instances])

    def do_update(self, arg):
        """
        Update an instance's attribute.

        Updates the specified attribute of the instance.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.class_names:
            print("** class doesn't exist **")
            return

        if len(args) <= 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) <= 2:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) <= 3:
            print("** value missing **")
            return

        attribute_value_str = args[3]

        # Try to cast the attribute value to the appropriate type
        attribute_value = None
        try:
            attribute_value = eval(attribute_value_str)
        except Exception as e:
            print(f"** invalid value: {e} **")
            return

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
