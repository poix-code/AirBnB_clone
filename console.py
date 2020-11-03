#!/usr/bin/python3
"""Program to execute a cmd console"""
import cmd


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
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """Function to exit the console"""
        print("")
        return True

    def help_EOF(self):
        """Function to document help section"""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """Does not execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
