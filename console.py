#!/usr/bin/python3
""" Module contains the entry point of the command interpreter
"""

import cmd
import os

from models import storage
from models.base_model import BaseModel

from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """inherits the Cmd class"""

    prompt = "(hbnb) "
    ids = []

    def do_EOF(self, line):
        """exits the interpreter if EOF reached"""

        print("")
        return True

    def do_quit(self, line):
        """exits if quit command is executed"""

        return True

    def emptyline(self):
        """return empty string if the line is empty"""

        return ""

    def do_create(self, line):
        """creates a new BaseModel instance"""

        if line == "":
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            storage.reload()
            storage.new(instance)
            instance.save()
            HBNBCommand.ids.append(instance.id)
            print(instance.id)

    def do_show(self, line):
        """shows the string representation of the given instance'id"""

        from models.engine.file_storage import FileStorage

        if line == "" or len(line.split()) == 0:
            print("** class name missing **")

        elif len(line.split()) < 2:
            if "-" in line:
                print("** class name missing **")
            elif "BaseModel" not in line:
                print("** class doesn't exist **")
            elif "BaseModel" in line:
                print("** instance id missing **")

        else:
            if line.split()[0] != "BaseModel":
                print("** class doesn't exist **")
            elif line.split()[1] not in HBNBCommand.ids:
                print("** no instance found **")
            else:
                instance_id = line.split()[1]
                for k, v in storage.__objects.items():
                    if instance_id in k:
                        print(storage.__objects[k])
                        break


    def do_destroy(self, line):
        """destroys an instance"""

        if line == "" or len(line.split()) == 0:
            print("** class name missing **")

        elif len(line.split()) < 2:
            if "-" in line:
                print("** class name missing **")
            elif "BaseModel" not in line:
                print("** class doesn't exist **")
            elif "BaseModel" in line:
                print("** instance id missing **")

        else:
            if line.split()[0] != "BaseModel":
                print("** class doesn't exist **")
            elif line.split()[1] not in HBNBCommand.ids:
                print("** no instance found **")
            else:
                instance_id = line.split()[1]
                for k, v in storage.__objects.items():
                    if instance_id in k:
                        storage.__objects.pop(k)
                        HBNBCommand.ids.remove(instance_id)
                        os.remove(storage.__file_path)
                        storage.save()
                        break


    def do_all(self, line):
        """Prints all string representation of all instances"""

        instances = []

        if len(line.split()) == 0 or line.split()[0] == "BaseModel":
            for k, v in storage._FileStorage__objects.items():
                instances.append(str(v))
            print(instances)
        else:
            print("** class doesn't exist **")

    # def do_update(self, line):
    #     """updates instance's attributes"""


    #     if len(line) == 0:
    #         print("** class name missing **")
    #     elif line.split()[0] != "BaseModel":
    #         print("** class doesn't exist **")
    #     elif len(line.split()) == 1:
    #         print("** instance id missing **")
    #     elif line.split()[1] not in "".join(storage._FileStorage__objects.keys()):
    #         print("** no instance found **")
    #     elif len(line.split()) == 2:
    #         print("** attribute name missing **")
    #     elif len(line.split()) == 3:
    #         print("** value missing **")
    #     else:
    #         name = line.split()[2]
    #         value = line.split()[3]
    #         for k, v in storage._FileStorage__objects.items():
    #             if line.split()[1] in k:
    #                 v[str(name)] = value
    #                 break


if __name__ == '__main__':
    HBNBCommand().cmdloop()

