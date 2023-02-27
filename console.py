#!/usr/bin/python3
import cmd
import sys
import os
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command line for work in front and backend"""

    prompt = '(hbnb) '
    file = None
    classes = {'BaseModel': BaseModel}

    def emptyline():
        """nothing when empty argument and enter"""
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """ End of file ctrl +d"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id."""
        if len(args) < 1:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            ninstance = eval(args[0])()
            ninstance.save()
            print(ninstance.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, argv):
        """Prints the string representation of an
        instance based on the class name and id"""
        enter = argv.split()
        if enter == 0:
            print("** class name missing **")
        elif enter[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(enter) < 2:
            print("** instance id missing **")
        else:
            key = enter[0] + '.' + enter[1]
            storage.reload()
            if key not in storage.all():
                print("** no instance found **")
            else:
                objects = storage.all()
                if key in objects.keys():
                    print(objects[key])


if __name__ == '__main__':
    """infinity loops"""
    HBNBCommand().cmdloop()
