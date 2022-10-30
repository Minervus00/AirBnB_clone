#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python39/python.exe
# /usr/bin/python3
"""Module containing the command interpreter program"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """The command interpreter class"""
    prompt = "(hbnb) "

    def do_create(self, argu):
        """Creates a new instance of BaseModel, saves it (JSON)
        and prints id. Ex: $ create BaseModel"""
        if not argu:
            print("** class name missing **")
        elif argu != "BaseModel":
            print("** class doesn't exist **")
        else:
            dum = BaseModel()
            dum.save()
            print(dum.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234"""
        arg = arg.split()
        if valid(arg):
            tmp_dic = storage._FileStorage__objects.get(f"{arg[0]}.{arg[1]}")
            if (tmp_dic):
                print(BaseModel(**tmp_dic))
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (update the JSON file). Ex: $ destroy BaseModel 1234-1234-1234"""
        arg = arg.split()
        if valid(arg):
            dc = storage._FileStorage__objects.pop(f"{arg[0]}.{arg[1]}", False)
            if not dc:
                print("** no instance found **")
            else:
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all"""
        dic = storage._FileStorage__objects
        if arg:
            arg = arg.split()
            if len(arg) != 1:
                print("** class doesn't exist **")
            else:
                resu = []
                for k, v in dic.items():
                    if k.startswith(arg[0]):
                        resu.append(str(BaseModel(**v)))
                if resu:
                    print(resu)
                else:
                    print("** class doesn't exist **")
        else:
            resu = []
            for k, v in dic.items():
                resu.append(str(BaseModel(**v)))
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
        elif arg[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        elif length >= 2 and not dic.get(f"{arg[0]}.{arg[1]}", False):
            print("** no instance found **")
        elif length == 2:
            print("** attribute name missing **")
        elif length == 3:
            print("** value missing **")
        else:
            dic[f"{arg[0]}.{arg[1]}"][f"{arg[2]}"] = f"{arg[4]}"
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
    if not arg:
        print("** class name missing **")
        check = False
    elif arg[0] not in ["BaseModel"]:
        print("** class doesn't exist **")
        check = False
    elif len(arg) != 2:
        print("** instance id missing **")
        check = False
    return check


if __name__ == '__main__':
    HBNBCommand().cmdloop()
