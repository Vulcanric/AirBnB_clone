#!/usr/bin/python3
"""
This file contains the FileStorage engine class used in storing data
Check it out!
Also, check the `models/__init__.py` file for a special instance of this class
Also see it used in `models/base_model.py`.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class FileStorage:
        Defines methods, attributes and functionalities used in saving data
        into files for persistency and quick recovery of objects.

        Its basic function is to serialize/encode and deserialize/decode data
        in and out of a JSON file for use.

        The aim is to convert objects into dictionaries, pass this dictionaries
        to JSON-dump to convert(serialize) them into strings, so they can be
        stored in files.
        Next is to read these strings from the files, convert them back into
        Python dictionaries using JSON-load and create objects from those dict-
        ionaries. Simple right :)

        For better understanding, the flow of Serialization-deserialization is:
            ```
            <class 'User'> -> to_dict() -> <class dict> -> JSON dump ->
             <class 'str'> -> FILE -> <class 'str'> -> JSON load ->
            <class 'dict'> -> <class 'User'>
            ```
    """
    __file_path = "file.json"  # File to store data
    __objects = {}  # Temporary storage for all objects

    def all(self):
        """ Returns all objects via the dictionary `__objects`"""
        return self.__objects

    def new(self, obj):
        """
        Set in a new object into `__objects` by the key:
        <obj class name>.id
        """
        objkey = f"{obj.to_dict()['__class__']}.{obj.id}"
        self.__objects.update({objkey: obj})

    def save(self):
        """ Serializes __objects to the JSON file `__file_path` """
        # Convert each object in self.__objects to their dict representation
        # So they can be serialized(converted to JSON string)
        objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        # Get the string representation from __file_path, deserialize them into
        # Python dictionaries and create objects from those dictionaries
        # and save them in __objects
        try:
            f = open(self.__file_path, "r")
        except FileNotFoundError:
            pass
        else:
            objects_dict = json.load(f)
            f.close()
            for key, obj_dict in objects_dict.items():
                obj_class = key.split('.')[0]  # key = "<obj-class-name>'.'<obj-id>"
                obj = globals()[obj_class](**obj_dict)  # Recreate the object from its class
                self.new(obj)  # Add this object in the __objects dictionary
