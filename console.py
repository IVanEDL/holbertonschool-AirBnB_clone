#!/usr/bin/python3
import cmd
import sys
import os
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command line for work in front and backend"""

    prompt = '(hbnb) '
    file = None
    classes = {'BaseModel': BaseModel}

    def emptyline(self):
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
        if not enter:
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

    def do_destroy(self, argv):
        """Deletes an instance based on the class name and id"""
        input = argv.split()
        if not input:
            print("** class name missing **")
        elif input[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        elif len(input) < 2:
            print("** instance id missing **")
        else:
            key = input[0] + '.' + input[1]
            storage.reload()
            if key not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(key)
        
    def do_all(self, argv):
        input = argv.split()
        if not input:
            print(list(storage.all()))
        elif input[0] not in HBNBCommand.classes.keys():
            print("** class doesn't exist **")
        else:
            list_all = []
            for o_id in storage.all().keys():
                if o_id.split(".")[0] == input[0]:
                    list_all.append(str(storage.all()[o_id]))
            print(list_all)

    def do_update(self, argv):
        enter = argv.split()
        if not enter:
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
            elif len(enter) < 3:
                print("** attribute name missing **")
            elif len(enter) < 4:
                print("** value missing **")
            else:
                setattr(storage.all()[key], enter[2], enter[3])
                storage.save()

if __name__ == '__main__':
    """infinity loops"""
    HBNBCommand().cmdloop()
