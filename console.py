#!/usr/bin/python3
import cmd, sys, os



class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    file = None

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
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
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

    def do_show(args):
        pass

if __name__ == '__main__':
        HBNBCommand().cmdloop()
