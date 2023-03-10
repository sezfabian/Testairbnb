#/usr/bin/python3
"""File Storage Module"""
import json
import datetime
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def classes(self):
        from base_model import BaseModel
        classes = {"BaseModel": BaseModel}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                    {"id": str,
                     "created_at": datetime.datetime,
                     "updated_at": datetime.datetime}
                    }
        return attributes

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict, file)

    def reload(self):
        if os.path.isfile(self.__file_path) is True and os.path.getsize(self.__file_path) != 0:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                FileStorage.__objects.update(obj_dict)
