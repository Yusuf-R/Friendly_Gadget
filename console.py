#!/usr/bin/env python3
"""Management console for the Friendly Gadget project"""

import ast
import cmd
import json
import re
import shlex
from models.brand import Brand
from models.model import Model
from models.feature import Feature
from models.secondary_feature import Secondary
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
        return

    """Important Management functions"""

    def do_create_brand(self, argz):
        """Creates a new instance of a class"""
        usage = "Usage: create_brand <brand_name>"
        hint = "argument must be a string or a list of strings"
        list_hint = ["[", "]"]
        dict_hint = ["{", '}']
        # check if argumments is empty
        if argz is None or argz == "":
            print("Error: Brand name cannot be empty\n{}".format(usage))
            return
        # check if a list was passed as argument
        if argz[0] in list_hint:
            try:
                data = ast.literal_eval(argz)
                # clean the data for any inconsistency
                clean_data = []
                for brand in data:
                    clean_brand = re.sub(" +", " ", brand).strip()
                    clean_data.append(clean_brand)
                # check if brand name already exists
                for brand in clean_data:
                    if check_brand_name(brand):
                        print("Error: Brand name: {} already exists\n{}"
                              .format(brand, usage))
                        continue
                    # create a new brand
                    obj = Brand()
                    obj.brand_name = brand
                    obj.save()
                    print("Brand: {} created successfully\n{}\n"
                          .format(obj.brand_name, obj.id))
                return
            except Exception:
                print("Argument is erronously inconsistent\n{}".format(hint))
                return
        # check if string is surrounded by braces
        if argz[0] in dict_hint:
            print("We got a dictionary\n{}".format(hint))
            return
        # check if a string was passed in quotes
        if argz[0] in ["'", '"']:
            # ensuring only comma and space separated string
            if "," in argz and " " in argz:
                argz_synthesis = argz.replace(",", " ").split(" ")
                for brand in argz_synthesis:
                    if brand in ["'", '"', ""] or brand == "":
                        continue
                    brand = brand.strip("\"'")
                    if check_brand_name(brand):
                        print("Error: Brand name: {} already exists\n{}"
                              .format(brand, hint))
                        continue
                    obj = Brand()
                    obj.brand_name = brand
                    obj.save()
                    print("Brand {} created successfully\n{}\n"
                          .format(obj.brand_name, obj.id))
                return
            # ensuring only comma separated strings
            elif "," in argz and " " not in argz:
                argz_synthesis = argz.replace(",", " ").split(" ")
                for brand in argz_synthesis:
                    brand = brand.strip("\"'")
                    if check_brand_name(brand):
                        print("Error: Brand name: {} already exists\n{}"
                              .format(brand, usage))
                        continue
                    obj = Brand()
                    obj.brand_name = brand
                    obj.save()
                    print("Brand {} created successfully\n{}\n"
                          .format(obj.brand_name, obj.id))
                return
            # ensuring only spaces separated strings
            elif " " in argz and "," not in argz:
                argz_synthesis = argz.split(" ")
                for brand in argz_synthesis:
                    brand = brand.strip("\"'")
                    if brand == "":
                        continue
                    if check_brand_name(brand):
                        print("Error: Brand name: {} already exists\n{}"
                              .format(brand, usage))
                        continue
                    obj = Brand()
                    obj.brand_name = brand
                    obj.save()
                    print("Brand {} created successfully\n{}\n"
                          .format(obj.brand_name, obj.id))
                return
            # string should defintely just be a string
            else:
                argz = argz.strip("\"'")
                if check_brand_name(argz):
                    print("Error: Brand name: {} already exists\n{}"
                          .format(argz, usage))
                    return
                obj = Brand()
                obj.brand_name = argz
                obj.save()
                print("Brand {} created successfully\n{}\n"
                      .format(obj.brand_name, obj.id))
                return

        # single string without quotes
        if argz[0].isalpha():
            data = re.split(r'[,\s]+', argz.strip())
            for brand in data:
                if brand == "":
                    continue
                if check_brand_name(brand):
                    print("Error: Brand name: {} already exists\n{}"
                          .format(brand, usage))
                    continue
                obj = Brand()
                obj.brand_name = brand
                obj.save()
                print("Brand {} created successfully\n{}\n".
                      format(obj.brand_name, obj.id))
            return
        print("Error: Erronous data entry\n{}\n{}".format(usage, hint))
        return

    def do_create_model(self, argz):
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
        # validate if model_name already exists
        if check_model_name(model_name):
            print("Error: Model name: {} already exists\n{}"
                  .format(model_name, usage))
            return
        obj = Model()
        obj.model_name = model_name
        obj.brand_id = brand_id
        obj.save()
        print(
            "Model {} created successfully\n{}\n".format(
                obj.model_name, obj.id
            )
        )
        return

    def do_create_feature(self, argz):
        """Create a feautre for a given phone model"""
        usage = "Usage: <model_id> {<feature_key>: <feature_value>}"
        # check if argumments is empty
        if argz is None or argz == "":
            print("Error: Data stream is required\n{}".format(usage))
            return
        # check if id was print
        data = argz.strip("'\"").split(" ", 1)
        if len(data) == 1:
            print("Error: Feature attributes is required\n{}".format(usage))
            return
        id = data[0]
        dict_ = data[1]
        # Validate model_id
        if storage.get(Model, id) is None:
            print("Error: Invalid model id")
            return
        # Convert the dictionary portion into a dictionary
        try:
            dict_ = eval(dict_)
        # validate dictonary
        except Exception:
            print("Here: Error: Feature data must be a dictionary\n{}".format(usage))
            return

        if not isinstance(dict_, dict):
            print("HAAAHHHA: Error: Feature data must be a dictionary\n{}".format(usage))
            return
        # Create a new instance of Features
        obj = Feature()
        obj.model_id = id
        for key, val in dict_.items():
            setattr(obj, key, val)
        obj.save()
        print("Feature obj created successfully\n{}\n".format(obj.id))
        try:
            # we also instantiate the secondary features
            for _, val in dict_.items():
                if isinstance(val, dict):
                    for sec_key, sec_val in val.items():
                        secondary_entry = Secondary()
                        secondary_entry.feature_id = obj.id
                        secondary_entry.inner_key = sec_key
                        secondary_entry.inner_value = sec_val
                        secondary_entry.save()
                        print("Secondary obj created successfully\n{}\n"
                              .format(secondary_entry.id))
            return
        except Exception:
            print("BANGA Error: Feature data must be a dictionary of dictionary\n{}"
                  .format(usage))

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

    def help_show(self):
        """
        This will print out the dictionary of the all the attributes
        of a given class and it's id
        show documentation
        """
        usage = "show Brand f0ca205f-31dc-40e4-ac82-09a83d75bcaa"
        print("show <class> <id>")
        print("id is the id of the obj\nExample: {}".format(usage))
        return

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
        if len(tokens) == 3:
            print("Error: Missing value\n{}".format(usage))
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
        obj = storage.get(FgCmd.__clx[clx], id)
        val = val.strip("\"'")
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
            if attr == "model_name" or attr == "model_img":
                setattr(obj, attr, val)
                storage.save()
                print("{} Object updated successfully".format(clx))
                return
            else:
                print("Error: Invalid attribute\n{}".format(usage))
                return

    def do_all_specific(self, argz):
        """
        This will query the db and return all the child obj
        for a given parent id
        """
        usage = "Usage: all_specific <child class> <Parent-id>"
        tokens = shlex.split(argz)
        if len(tokens) == 0:
            print("Error: Missing class name\n{}".format(usage))
            return
        if len(tokens) == 1:
            print("Error: Missing object id\n{}".format(usage))
            return
        clx = tokens[0]
        id = tokens[1]
        # validate class name
        if clx not in FgCmd.__clx:
            print("Error: Invalid class name")
            return
        if FgCmd.__clx[clx] == Brand:
            print("This operation is forbidden for this class\n{}"
                  .format(usage))
            return
        if FgCmd.__clx[clx] == Model:
            # validate the id against Brand
            if storage.get(Brand, id) is None:
                print("Error: Invalid id for the class Brand")
                return
            FgCmd.action_specific(clx, id)
            return
        elif FgCmd.__clx[clx] == Feature:
            # valideate the id agains Model
            if storage.get(Model, id) is None:
                print("Error: Invalid id for the class Model")
                return
            FgCmd.action_specific(clx, id)
            return
        elif FgCmd.__clx[clx] == Secondary:
            # validate the id agains Feature
            if storage.get(Feature, id) is None:
                print("Error: Invalid id for the class Feature")
                return
            FgCmd.action_specific(clx, id)
            return
        return

    @staticmethod
    def action_specific(clx, id):
        obj_list = []
        data = storage.all(FgCmd.__clx[clx]).values()
        if data is None:
            print("No objects found")
            return
        for obj in data:
            obj_dict = obj.to_dict()
            if obj_dict["brand_id"] == id:
                obj_list.append(obj_dict)
            else:
                continue
            for disp in obj_list:
                print(disp)
                # print()
            obj_list = []
        return


def check_brand_name(name):
    """
    This function will helpe check if
    a band_name already exist in the database
    """
    all_obj = storage.all(Brand)
    for obj in all_obj.values():
        if obj.brand_name == name:
            return True
        else:
            continue
    return False


def check_model_name(name):
    """
    This function will helpe check if
    a model_name already exist in the database
    """
    all_obj = storage.all(Model)
    for obj in all_obj.values():
        if obj.model_name == name:
            return True
        else:
            continue
    return False


if __name__ == "__main__":
    FgCmd().cmdloop()
