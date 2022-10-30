#!/usr/bin/python3
"""Module containing the command interpreter program"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The command interpreter class"""
    prompt = "(hbnb) "
    # authObj = authorized classes
    authObj = [
        "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_create(self, argu):
        """Creates a new instance of BaseModel, saves it (JSON)
        and prints id. Ex: $ create BaseModel"""
        argu = argu.split()
        if not argu:
            print("** class name missing **")
        elif argu[0] not in self.authObj:
            print("** class doesn't exist **")
        else:
            dum = eval(argu[0] + "()")
            dum.save()
            print(dum.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        arg = arg.split()
        if valid(arg):
            tmp_dic = storage._FileStorage__objects.get(f"{arg[0]}.{arg[1]}")
            print(tmp_dic)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (update the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        arg = arg.split()
        if valid(arg):
            storage._FileStorage__objects.pop(f"{arg[0]}.{arg[1]}")
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all"""
        dic = storage._FileStorage__objects
        arg = arg.split()
        if arg and arg[0] not in self.authObj:
            print("** class doesn't exist **")
        else:
            resu = []
            for k, v in dic.items():
                if arg and arg[0] not in k:
                    continue
                resu.append(str(v))
            if resu:
                print(resu)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"""
        dic = storage._FileStorage__objects
        arg = arg.split()
        length = len(arg)
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.authObj:
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        elif length >= 2 and f"{arg[0]}.{arg[1]}" not in dic.keys():
            print("** no instance found **")
        elif length == 2:
            print("** attribute name missing **")
        elif length == 3:
            print("** value missing **")
        else:
            if arg[3].count('"') == 1:
                arg[3] += " " + arg[4]
            setattr(dic[f"{arg[0]}.{arg[1]}"], arg[2], arg[3].replace('"', ''))
            storage.save()

    def emptyline(self):
        pass

    def do_quit(self, s):
        """Quit command to exit the program\n"""
        return True
    do_EOF = do_quit


def valid(arg):
    """Returns True if the command line is valid,
    otherwise False and prints the error"""
    check = True
    dic = storage._FileStorage__objects
    length = len(arg)
    if not arg:
        print("** class name missing **")
        check = False
    elif arg[0] not in HBNBCommand.authObj:
        print("** class doesn't exist **")
        check = False
    elif length == 1:
        print("** instance id missing **")
        check = False
    elif f"{arg[0]}.{arg[1]}" not in dic.keys():
        print("** no instance found **")
        check = False
    return check


if __name__ == '__main__':
    HBNBCommand().cmdloop()
