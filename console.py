#!/usr/bin/python3
"""
Module contains the entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
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
        """exits the interpreter if the "quit" command is executed"""

        return True

    def emptyline(self):
        """returns (prints) an empty string if the line is empty"""

        return ""

    def do_create(self, line):
        """creates a new BaseModel instance"""

        if line == "":
            print("** class name missing **")
        elif line not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                instance = BaseModel()
            elif line == "User":
                instance = User()

            storage.new(instance)
            instance.save()
            HBNBCommand.ids.append(instance.id)
            print(instance.id)

    def do_show(self, line):
        """shows the string representation of the given instance's id"""

        if line == "" or len(line.split()) == 0:
            print("** class name missing **")

        elif len(line.split()) < 2:
            if "-" in line:
                print("** class name missing **")
            elif "BaseModel" not in line or "User" not in line:
                print("** class doesn't exist **")
            elif "BaseModel" in line or "User" in line:
                print("** instance id missing **")

        else:
            if line.split()[0] not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
            elif line.split()[1] not in HBNBCommand.ids:
                print("** no instance found **")
            else:
                instance_id = line.split()[1]
                for k, v in storage._FileStorage__objects.items():
                    if instance_id in k:
                        print(storage._FileStorage__objects[k])
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
            if line.split()[0] != "BaseModel" or line.split()[0] != "User":
                print("** class doesn't exist **")
            elif line.split()[1] not in HBNBCommand.ids:
                print("** no instance found **")
            else:
                instance_id = line.split()[1]
                for k, v in storage._FileStorage__objects.items():
                    if instance_id in k:
                        storage._FileStorage__objects.pop(k)
                        HBNBCommand.ids.remove(instance_id)
                        storage.save()
                        break

    def do_all(self, line):
        """Prints all string representation of all instances"""

        instances = []

        if len(line.split()) == 0 or line.split()[0] in ["BaseModel", "User"]:
            for k, v in storage._FileStorage__objects.items():
                instances.append(str(v))
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """updates instance's attributes"""

        if len(line) == 0:
            print("** class name missing **")
        elif line.split()[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line.split()) == 1:
            print("** instance id missing **")
        elif line.split()[1] not in "".join(storage._FileStorage__objects.keys()):
            print("** no instance found **")
        elif len(line.split()) == 2:
            print("** attribute name missing **")
        elif len(line.split()) == 3:
            print("** value missing **")
        else:
            name = line.split()[2]
            value = line.split()[3]

            if value[0] in ["\'", "\""] and value[-1] not in ["\'", "\""]:
                for i in range(4, len(line.split())):
                    value += " " + line.split()[i]
                    if line.split()[i][-1] in ["\'", "\""]:
                        break
            if value[0] in ["\'", "\""]:
                value = value[1:-1]

            for k, v in storage._FileStorage__objects.items():
                if line.split()[1] in k:
                    v.__setattr__(name, value)
                    v.save()
                    break


if __name__ == '__main__':
    HBNBCommand().cmdloop()

