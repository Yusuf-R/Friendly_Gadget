#!/usr/bin/env python3
"""Management console for the Friendly Gadget project"""

import cmd
import json
import shlex
from models.brand import Brand
from models.model import Model
from models.feature import Feature
from models.secondary_features import Secondary
from models import storage


class FgCmd(cmd.Cmd):
    """FgConsole Module"""

    __clx = {
        "Model": Model,
        "Brand": Brand,
        "Feature": Feature,
        "Secondary": Secondary,
    }

    def __init__(self):
        """The constructor for HBNBCommand class."""
        super().__init__()
        self.prompt = "[FreindlyGadget]: "

    def do_EOF(self, arg):
        """Exits console"""
        print("\nExiting....\nDone")
        return True

    def help_EOF(self):
        """EOF documenataion"""
        print("Syntax: Ctrl + D")
        print("Terminates the program")

    def emptyline(self):
        """overwriting the emptyline method"""
        return False

    def help_emptyline(self):
        """emptyline doucmentation"""
        print("Ignores empty lines")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Quiting console...")
        return True

    def help_quit(self):
        """quit documentation"""
        print("Syntax: quit")
        print("Terminates and exit the program")

    """Important Management functions"""

    def do_create_brand(self, argz):
        """Creates a new instance of a class"""
        usage = "Usage: create_brand <brand_name>"
        argz = argz.strip("\"'").split()
        if len(argz) == 0:
            print("Error: Name of brand cannot be empty\n{}".format(usage))
            return
        for data in argz:
            data = data.strip("\"'")
            obj = Brand()
            obj.brand_name = data
            obj.save()
            print(
                "Brand {} created successfully\n{}\n".
                format(obj.brand_name, obj.id)
                )
        return

    def do_create_models(self, argz):
        """Creates a new instance of a class"""
        usage = "Usage: create_model <obj_name> <brand_id>"
        argz = argz.strip("\"'").split()
        if len(argz) == 0:
            print("Error: Name of model cannot be empty\n{}".format(usage))
            return
        if len(argz) == 1:
            print("Error: brand id required\n{}".format(usage))
            return
        if len(argz) > 2:
            print("Error: Too many arguments\n{}".format(usage))
            return
        model_name = argz[0].strip("\"'")
        brand_id = argz[1].strip("\"'")
        # validate brand_id
        if storage.get(Brand, brand_id) is None:
            print("Error: Invalid brand id")
            return
        obj = Model()
        obj.model_name = model_name
        obj.brand_id = brand_id
        obj.save()
        print(
            "Model {} created successfully\n{}\n".
            format(obj.model_name, obj.id)
        )
        return

    def do_create_features(self, argz):
        """Create a feautre for a given phone model"""
        usage = "Usage: <model_id> {<feature_key>: <feature_value>}"

        # Split the data into ID and dictionary portion
        id, dict_ = argz.split(" ", 1)
        # Remove any extra spaces and newlines from the dictionary portion
        dict_ = dict_.strip()
        if id is None:
            print("Error: Model id required\n{}".format(usage))
            return
        if dict_ is None:
            print("Error: Feature data required\n{}".format(usage))
            return
        # Validate model_id
        if storage.get(Model, id) is None:
            print("Error: Invalid model id")
            return
        # Convert the dictionary portion into a dictionary
        dict_ = eval(dict_)
        # validate dictonary
        if not isinstance(dict_, dict):
            print("Error: Feature data must be a dictionary\n{}".format(usage))
            return
        # Create a new instance of Features
        obj = Feature()
        obj.model_id = id
        for key, val in dict_.items():
            setattr(obj, key, val)
        obj.save()
        print("Feature obj created successfully\n{}\n".format(obj.id))

        # we also instantiate the secondary features
        for _, val in dict_.items():
            if isinstance(val, dict):
                for sec_key, sec_val in val.items():
                    secondary_entry = Secondary()
                    secondary_entry.feature_id = obj.id
                    secondary_entry.inner_key = sec_key
                    secondary_entry.inner_value = sec_val
                    secondary_entry.save()
        print("Secondary obj created successfully\n{}\n".
              format(secondary_entry.id))
        return

    def do_show(self, argz):
        """
        Prints the string representation of an instance
        show <class> <id>
        """
        usage = "Usage: show <class> <id>"
        tokens = shlex.split(argz)
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) == 1:
            print("Error: Missing object id\n{}".format(usage))
            return
        if len(tokens) > 2:
            print("Error: Too many arguments\n{}".format(usage))
            return
        clx = tokens[0]
        id = tokens[1]
        # validate class name
        if clx not in FgCmd.__clx:
            print("Error: Invalid class name")
            return
        # validate id
        if storage.get(FgCmd.__clx[clx], id) is None:
            print("Error: Invalid id")
            return
        obj = storage.get(FgCmd.__clx[clx], id)
        print(obj.to_dict())


    def do_delete(self, argz):
        """Delete content from the database"""
        usage = "Usage: delete <class> <id>"
        tokens = shlex.split(argz)
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) == 1:
            print("Error: Missing object id\n{}".format(usage))
            return
        if len(tokens) > 2:
            print("Error: Too many arguments\n{}".format(usage))
            return
        clx = tokens[0]
        id = tokens[1]
        # validate class name
        if clx not in FgCmd.__clx:
            print("Error: Invalid class name")
            return
        # validate id
        if storage.get(FgCmd.__clx[clx], id) is None:
            print("Error: Invalid id")
            return
        # get the object
        obj = storage.get(FgCmd.__clx[clx], id)
        storage.delete(obj)
        storage.save()
        print("Object deleted successfully")
        return


    def do_all(self, argz):
        """Prints all string representation of all instances"""
        usage = "Usage: all <class>"
        tokens = shlex.split(argz)
        obj_list = []
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) > 1:
            print("Error: Too many arguments\n{}".format(usage))
            return
        clx = tokens[0]
        # validate class name
        if clx not in FgCmd.__clx:
            print("Error: Invalid class name")
            return
        # get the objects
        objs = storage.all(FgCmd.__clx[clx])
        if len(objs) == 0:
            print("No objects found")
            return
        for obj in objs.values():
            obj_list.append(obj.to_dict())
        for disp in obj_list:
            print(disp)
            print()
        return

    def do_update(self, argz):
        """Update a given object"""
        usage = "Usage: update <class=Aaaaa> <id> <attribute> <value>"
        tokens = shlex.split(argz)
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) == 1:
            print("Error: Missing object id\n{}".format(usage))
            return
        if len(tokens) == 2:
            print("Error: Missing attribute\n{}".format(usage))
            return
        clx = tokens[0]
        id = tokens[1]
        attr = tokens[2]
        val = tokens[3]
        # validate class name
        if clx not in FgCmd.__clx:
            print("Error: Invalid class name")
            return
        # validate id
        if storage.get(FgCmd.__clx[clx], id) is None:
            print("Error: Invalid id")
            return
        if clx == "Feature":
            usage = "Usage: update <class> <id> <attribute> <value>"
            if len(tokens) == 3:
                print("Error: Missing value\n{}".format(usage))
                return
            val = argz.split(" ", 3)[3]
            if val is None:
                print("Error: Feature data required\n{}".format(usage))
                return
            # Convert the dictionary portion into a dictionary
            val = val.strip("\"'")
            val = val.replace("'", '"')
            try:
                val = json.loads(val)
            except Exception:
                print(
                    "Error: Feature data must be a dictionary\n{}".format(
                        usage
                    )
                )
                return
            # get the object
            obj = storage.get(FgCmd.__clx[clx], id)
            # set the attribute
            setattr(obj, attr, val)
            storage.save()
            print("{} object updated successfully".format(clx))
            # update secondary likewise
            return
        if clx == "Secondary":
            usage = "Usage: update <class> <value>"
            val = argz.split(" ", 2)[2]
            if val is None:
                print("Error: Secondary data required\n{}".format(usage))
                return
            # Convert the dictionary portion into a dictionary
            val = val.strip("\"'")
            val = val.replace("'", '"')
            try:
                val = json.loads(val)
            except Exception:
                print(
                    "Error: Feature data must be a dictionary\n{}".format(
                        usage
                    )
                )
                return
            # get the object
            obj = storage.get(FgCmd.__clx[clx], id)
            # set the attribute
            for s_k, s_v in val.items():
                obj.inner_key = s_k
                obj.inner_value = s_v
            storage.save()
            print("Secondary object updated successfully")
            return
        # get the object
        if clx not in FgCmd.__clx:
            print(
                "Error: Invalid class name\n{}\nPlease check the class name".format(
                    usage
                )
            )
            return
        obj = storage.get(FgCmd.__clx[clx], id)
        # set the attribute
        if clx == "Brand":
            if attr == "brand_name":
                setattr(obj, attr, val)
                storage.save()
                print("{} Object updated successfully".format(clx))
                return
            else:
                print("Error: Invalid attribute\n{}".format(usage))
                return
        if clx == "Model":
            if attr == "model_name":
                setattr(obj, attr, val)
                storage.save()
                print("{} Object updated successfully".format(clx))
                return
            else:
                print("Error: Invalid attribute\n{}".format(usage))
                return



if __name__ == "__main__":
    FgCmd().cmdloop()
