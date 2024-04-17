import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    def do_help(self, arg):
        if arg:
            super().do_help(arg)
        else:
            print("Help documentation goes here")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
