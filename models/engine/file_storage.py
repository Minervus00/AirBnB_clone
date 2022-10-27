#!/usr/bin/python3
"""Module conatining the class FileStorage"""
from json import dumps, loads
from os.path import exists


class FileStorage:
    """Class that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file at the path __file_path"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            file.write(dumps(FileStorage.__objects))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as file:
                FileStorage.__objects = loads(file.read())
