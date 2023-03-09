#!/usr/bin/python3
""" Console 0.0.1 Module"""
import cmd

class HBNBCommand(cmd.Cmd):

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def do_greet(self, line):
        print("hi there")

if __name__ == '__main__':
    HBNBCommand().cmdloop()