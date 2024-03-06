#!/usr/bin/python3
"""
Contains the entry point of the command interpreter, called
HBNBCommand
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ The backend utility console class used to function as the console """

    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_EOF(self, line):
        """ Exit the program, similar to the quit function """
        return True

    def do_quit(self, line):
        """
        Exit the program, common to the EOF function
        SYNOPSIS: quit
        """
        return True

    def emptyline(self):
        """
        Overwrite the emptyline function to do nothing when an empty
        line is passed in response to the prompt
        """
        pass

    def do_create(self, line):
        """
    Creates a new instance of a class and print out the id of the instance
    SYNOPSIS: create <object-classname>
    Classes of objects that can be created:
        BaseModel
        User - Create a new user object
        State - Create a new state object
        City - Create a new city object
        Place - Create a new place object
        """
        class_name = line
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = globals()[class_name]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
    Prints the string representation of an instance based on the
    class name and id
    SYNOPSIS: show <class-name> <obj-id>
    EX: show BaseModel 1234-1234-1234
        """
        # Validations
        if not line:  # No class name specified: $ show
            print("** class name missing **")
        elif line.split(' ')[0] not in self.classes:  # class not real class
            print("** class doesn't exist **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        else:
            # Remake object key from <obj class name> and <obj id>
            obj_key = line.replace(' ', '.')  # 'BaseModel 12'->'BaseModel.12'
            all_objects = storage.all()  # .all() = {"B.12":B_obj,"U.23":U_obj}
            try:
                print(all_objects[obj_key])
            except KeyError:  # If there's no such key
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and id
        SYNOPSIS: destroy <class-name> <obj-id>
        EX: destroy BaseModel 1234-1234-1234
        """
        # Validations
        if not line:
            print("** class name missing **")
        elif line.split(' ')[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(line.split(' ')) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            obj_key = line.replace(' ', '.')
            try:
                del all_objects[obj_key]
            except KeyError:  # If the key is not found in all_objects
                print("** no instance found **")
            finally:
                storage.save()  # Save the changes made, to json file

    def do_all(self, line):
        """
        Display all instance base on or not on a class name
        SYNOPSIS: all [instance-class]
        """
        # Get all objects
        all_objects = storage.all()

        list_of_objects = []

        # When no class name is passed, get all objects string representation
        if not line:
            list_of_objects = [obj.__str__() for obj in all_objects.values()]
        # When class name is passed but is not valid (such class doesn't exist)
        elif line not in self.classes:
            print("** class doesn't exist **")
            return False
        # When class name is passed and is valid
        else:
            for obj_key, obj in all_objects.items():
                if line in obj_key.split('.'):
                    list_of_objects.append(obj.__str__())

        print(list_of_objects)

    def do_update(self, line):
        """
        Update an instance based on the class name and id by adding or
        updating attribute
        SYNOPSIS: update <class name> <id> <attribute name> "<attribute value>"
        """
        all_objects = storage.all()

        object_details = shlex.split(line)  # split line shell way
        obj_class, obj_id, obj_key, attr_name, attr_value = '', '', '', '', ''
        try:
            obj_class = object_details[0]
            obj_id = object_details[1]
            obj_key = f"{obj_class}.{obj_id}"  # "User.1234-1234-1234"
            attr_name = object_details[2]
            attr_value = object_details[3]
        except:
            pass

        if obj_class == '':  # Object class was not entered
            print("** class name missing **")
        elif obj_class not in self.classes:  # Object class is not valid
            print("** class doesn't exist **")
        else:
            if obj_id == '':  # Object id was not entered
                print("** instance id missing **")
            elif obj_key not in all_objects.keys():  # Object is not found
                print(obj_key)
                print("** no instance found **")
            else:
                if attr_name == '':
                    print("** attribute name missing **")
                elif attr_value == '':
                    print("** value missing **")
                else:
                    ## Handle attribute value type
                    if attr_value.isdigit():
                        attr_value = int(attr_value)
                    # If value passed is a string
                    elif attr_value.isalpha():
                        pass
                    # If value passed is a float
                    elif attr_value[0].isdigit() and '.' in attr_value:
                        attr_value = float(attr_value)
        
                    # Update object with attribute
                    setattr(all_objects[obj_key], attr_name, attr_value)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
