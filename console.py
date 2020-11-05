#!/usr/bin/python3
"""Program to execute a cmd console"""
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']


class HBNBCommand(cmd.Cmd):
    """Defined the class"""
    prompt = '(hbnb) '
    use_rawinput = False
    file = None

    def do_quit(self, line):
        """Function to exit the console"""
        return True

    def help_quit(self):
        """Function to document help section"""
        print("Quit command to exit the program.\n")

    def do_EOF(self, line):
        """Function to exit the console"""
        print("")
        return True

    def help_EOF(self):
        """Function to document help section"""
        print("EOF command to exit the program.\n")

    def emptyline(self):
        """Does not execute anything"""
        pass

    def do_create(self, clss):
        """Creates a new instance of BaseModel"""
        if not clss:
            print("** class name missing **")
        elif globals().get(clss) is None:
            print("** class doesn't exist **")
        else:
            obj = eval(clss)()
            print(obj.id)
            obj.save()

    def help_create(self):
        """Function to document help section"""
        print("Creates a new instance BaseModel,\
save it in 'file.json' and prints its 'id'.\n")

    def do_show(self, clss):
        """Prints the string representation of an instance"""
        splitline = clss.split()
        cid = '.'.join(splitline)
        if not clss:
            print("** class name missing **")
        elif globals().get(splitline[0]) is None:
            print("** class doesn't exist **")
        elif len(splitline) == 1:
            print("** instance id missing **")
        elif cid not in models.storage.all():
            print("** no instance found **")
        else:
            print(models.storage.all()[cid])

    def help_show(self):
        """Function to document help section"""
        print("Prints the string representation of an\
 instance based on the class name and id.\n")

    def do_destroy(self, clss):
        """Deletes an instance"""
        splitline = clss.split()
        did = '.'.join(splitline)
        if not clss:
            print("** class name missing **")
        elif globals().get(splitline[0]) is None:
            print("** class doesn't exist **")
        elif len(splitline) == 1:
            print("** instance id missing **")
        elif did not in models.storage.all():
            print("** no instance found **")
        else:
            del models.storage.all()[did]
            models.storage.save()

    def help_destroy(self):
        """Function to document help section"""
        print("Deletes an instance based on the class name and id.\n")

    def do_all(self, clss):
        """Prints all string representation of all instances"""
        if not clss or globals().get(clss) is not None:
            l = []
            for model in models.storage.all():
                l.append(str(models.storage.all()[model]))
            print(l)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """Function to document help section"""
        print(" Prints all string representation of all instances\
 based or not on the class name.\n")

    def do_update(self, clss):
        """Updates an instance"""
        splitline = clss.split(' ')
        if not clss:
            print("** class name missing **")
            return
        elif globals().get(splitline[0]) is None:
            print("** class doesn't exist **")
            return
        elif len(splitline) == 1:
            print("** instance id missing **")
            return
        if len(splitline) == 3:
            print("** value missing **")
            return
        sid = splitline[0] + '.' + splitline[1]
        all_objs = storage.all()
        for key, value in all_objs.items():
            if sid in key:
                if len(splitline) == 2:
                    print("** attribute name missing **")
                    return
                if splitline[3][0] == "\"" and splitline[3][-1] == "\"":
                    setattr(value, splitline[2], splitline[3][1:-1])
                    storage.save()
                    return
                setattr(value, splitline[2], splitline[3])
                storage.save()
                return
        print("** no instance found **")

    def help_update(self):
        """Function to document help section"""
        print("Updates an instance based on the class name\
 and id by adding or updating attribute")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
