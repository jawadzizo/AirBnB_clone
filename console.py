#!/usr/bin/python3
"""
Module contains the entry point of the command interpreter
"""

import cmd
from models import storage
from models.user import User
from models.engine.file_storage import FileStorage

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


obj_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

class HBNBCommand(cmd.Cmd):
    """inherits the Cmd class"""

    prompt = "(hbnb) "
    ids = {
        "BaseModel" : [],
        "User" : [],
        "Place" : [],
        "State" : [],
        "City" : [],
        "Amenity": [],
        "Review" : []
    }

    def do_EOF(self, line):
        """exits the interpreter if EOF reached"""

        print("")
        return True

    def do_quit(self, line):
        """exits the interpreter if the "quit" command is executed"""

        return True

    def emptyline(self):
        """returns (prints) an empty string if the line is empty"""

        return ""

    def do_create(self, line):
        """creates a new object instance"""

        args = line.split()

        if line == "":
            print("** class name missing **")
        elif args[0] not in obj_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(f"{args[0]}()")
            storage.new(instance)
            storage.save()
            HBNBCommand.ids[args[0]].append(instance.id)
            print(instance.id)

    def do_show(self, line):
        """shows the string representation of the given instance's id"""

        args = line.split()

        if line == "":
            print("** class name missing **")
        elif args[0] not in obj_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[1] not in HBNBCommand.ids[args[0]]:
            print("** no instance found **")

        else:
            instance_id = args[1]
            for k, v in storage._FileStorage__objects.items():
                if instance_id in k and args[0] in k:
                    print(storage._FileStorage__objects[k])
                    break

    def do_destroy(self, line):
        """destroys an instance"""

        args = line.split()

        if line == "":
            print("** class name missing **")
        elif args[0] not in obj_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[1] not in HBNBCommand.ids[args[0]]:
            print("** no instance found **")

        else:
            instance_id = args[1]
            for k, v in storage._FileStorage__objects.items():
                if instance_id in k:
                    storage._FileStorage__objects.pop(k)
                    HBNBCommand.ids[args[0]].remove(instance_id)
                    storage.save()
                    break

    def do_all(self, line):
        """Prints all string representation of all instances"""

        args = line.split()
        instances = []

        if line == "":
            for k, v in storage._FileStorage__objects.items():
                instances.append(str(v))
            print(instances)

        elif args[0] not in obj_classes:
            print("** class doesn't exist **")

        else:
            for k, v in storage._FileStorage__objects.items():
                if args[0] in k:
                    instances.append(str(v))
            print(instances)

    def do_update(self, line):
        """updates instance's attributes"""

        args = line.split()

        if line == "":
            print("** class name missing **")
        elif args[0] not in obj_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[1] not in HBNBCommand.ids[line.split()[0]]:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            name = args[2]
            value = args[3]

            if value[0] in ["\'", "\""] and value[-1] not in ["\'", "\""]:
                for i in range(4, len(args)):
                    value += " " + args[i]
                    if args[i][-1] in ["\'", "\""]:
                        break
            if value[0] in ["\'", "\""]:
                value = value[1:-1]

            for k, v in storage._FileStorage__objects.items():
                if args[0] in k and args[1] in k:
                    v.__setattr__(name, value)
                    v.save()
                    break


if __name__ == '__main__':
    HBNBCommand().cmdloop()
