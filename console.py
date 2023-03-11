#!/usr/bin/python3
""" Console 0.0.1 Module"""
import cmd
from models.base_model import BaseModel
from models import FileStorage
storage = FileStorage()

class HBNBCommand(cmd.Cmd):

    __classes = {"BaseModel"}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def do_greet(self, line):
        print("hello, {}".format(line))

    def do_create(self, line):
        """Usage: create <class>"""
        """Creates a new class instance, saves it to the Json file and prints its id """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.__classes:
            print("** class doesn't exist **")
        else:
            my_model = eval(line)()
            storage.save()
            print(my_model.id)

    def do_show(self, line):
        """Usage: show <class name> <id>"""
        """Prints the string representation of an instance based on the class name and id"""
        my_args = line.split(" ")
        objects = storage.all()
        if len(my_args) == 0:
            print("** class name missing **")
        elif my_args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(my_args) != 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(my_args[0], my_args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                print("{}".format(objects[key]))

    def do_destroy(self, line):
        """Usage: show <class name> <id>"""
        """Deletes an instance based on the class name and id"""
        my_args = line.split(" ")
        objects = storage.all()
        if len(my_args) == 0:
            print("** class name missing **")
        elif my_args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(my_args) != 2:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(my_args[0], my_args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                FileStorage.__objects = objects
                storage.save()

    def do_all(self, line):
        """Usage: all <class name> or all"""
        """Prints all string representation of all instances based or not on the class name"""
        objects = storage.all()
        obj_out = []
        if len(line) == 0 :
            for v in objects.values():
                obj_out.append(v.__str__())
            print("{}".format(obj_out))
        elif line in self.__classes:
            for v in objects.values():
                if line == v.__class__.__name__:
                    obj_out.append(v.__str__())
            print(obj_out)

        elif line not in self.__classes:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> "<attribute value>""""
        """Updates an instance based on the class name and id by adding or updating attribute"""
        
        

    def do_clear(self, line):
        FileStorage.__objects = {}
        storage.save()
