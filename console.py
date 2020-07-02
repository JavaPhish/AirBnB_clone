#!/usr/bin/python3
""" console.py: Main entry point for the HBNB command interpreter """


import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand - Simple command tests """
    prompt = "(hbnb) "
    PossibleClasses = [
            "BaseModel",
            "City",
            "Review",
            "Amenity",
            "State",
            "Place",
            "User"]

    # Command methods
    def emptyline(self):
        """ emptyline: if an empty line is passed, do nothing """
        pass

    def do_quit(self, line):
        """ do_quit: Quit command """
        return True

    def do_EOF(self, line):
        """ do_EOF: End of File handling """
        print("")  # Print a new line, since EOF doesnt do that on its own
        return True

    def do_create(self, line):
        """ do_create: Create a new class """
        if line == "":
            print("** class name missing **")
        elif line == "BaseModel":
            NewInstance = BaseModel()
            NewInstance.save()
            print(NewInstance.id)
        elif line == "Amenity":
            NewInstance = Amenity()
            NewInstance.save()
            print(NewInstance.id)
        elif line == "City":
            NewInstance = City()
            NewInstance.save()
            print(NewInstance.id)
        elif line == "Place":
            NewInstance = Place()
            NewInstance.save()
            print(NewInstance.id)
        elif line == "Review":
            NewInstance = Review()
            NewInstance.save()
            print(NewInstance.id)
        elif line == "State":
            NewInstance = State()
            NewInstance.save()
            print(NewInstance.id)
        elif line == "User":
            NewInstance = User()
            NewInstance.save()
            print(NewInstance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ do_show: Print the string representation of an instance """
        splitted = line.split(" ")
        if len(splitted[0]) == 0:
            print("** class name missing **")
        elif splitted[0] in self.PossibleClasses:
            if len(splitted) == 2:
                for string, info in (models.storage.all()).items():
                    if string == "{}.{}".format(splitted[0], splitted[1]):
                        print(info)
                        return
                print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """ do_destroy: Print the string representation of an instance """
        splitted = line.split(" ")
        if len(splitted[0]) == 0:
            print("** class name missing **")
        elif splitted[0] in self.PossibleClasses:
            if len(splitted) == 2:
                for inst, i in (models.storage.all()).items():
                    # i goes unused, can't loop without it for some reason
                    if inst == "{}.{}".format(splitted[0], splitted[1]):
                        del models.storage.all()[inst]
                        models.storage.save()
                        return
                print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """ do_all: Print all instances, or all of a specific class """
        final = []
        splitted = line.split(" ")
        if len(line) == 0:  # No specific class given
            for string, info in (models.storage.all()).items():
                final.append(str(info))
            print(final)
            return
        if splitted[0] in self.PossibleClasses:
            for string, info in (models.storage.all()).items():
                if string.split(".")[0] == splitted[0]:
                    final.append(str(info))
            print(final)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ do_update: Updates an instance """
        splitted = line.split(" ")
        if len(splitted[0]) == 0:
            print("** class name missing **")
        elif splitted[0] in self.PossibleClasses:
            if len(splitted) >= 2:
                for ClassName, inst in (models.storage.all()).items():
                    # i goes unused, can't loop without it for some reason
                    if ClassName == "{}.{}".format(splitted[0], splitted[1]):
                        if len(splitted) == 2:
                            print("** attribute name missing **")
                            return
                        if len(splitted) == 3:
                            print("** value missing **")
                            return
                        if len(splitted) == 4:
                            caster = type(getattr(inst, splitted[2]))
                            setattr(inst, splitted[2], caster(splitted[3]))
                            inst.save()
                            return
                print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    # Help methods
    def help_quit(self):
        """ help_quit: Help documentation for quit """
        print("quit\nQuits the command prompt")

    def help_EOF(self):
        """ help_EOF: Help documentation for EOF """
        print("EOF\nHandles End of File(?)")

    def help_create(self):
        """ help_create: Help documentation for Create """
        print("create [Class name]\nCreate a new instance of a class")
        print("Classes:\nBaseModel\nAmenity\nCity\nPlace")
        print("Review\nState\nUser")

    def help_show(self):
        """ help_show: Help documentation for Show """
        print("show [Class name] [Id]\nShow information", end="")
        print("for an instance of a class")

    def help_destroy(self):
        """ help_destroy: Help documentation for Destroy """
        print("destroy [Class name] [Id]\nDestroy an instance of a class")

    def help_all(self):
        """ help_all: Help documentation for All """
        print("all [Class name]\nShow information for all instances", end="")
        print("or all instances of a class")

    def help_update(self):
        """ help_update: Help documentation for Update """
        print("update [Class name] [Id] [Attribute name] [New value]")
        print("Updates the attribute of an instance")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
