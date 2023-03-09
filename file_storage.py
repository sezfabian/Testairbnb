#/usr/bin/python3
"""File Storage Module"""
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj


    def save(self):
        with open(self.__file_path, "w", encoding="utf-8") as file:
            dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict, file)

