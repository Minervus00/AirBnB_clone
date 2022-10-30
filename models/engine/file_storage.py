#!/usr/bin/python3
"""Module conatining the class FileStorage"""
from json import dumps, loads
from os.path import exists
import models.base_model
import models.user
import models.state
import models.city
import models.amenity
import models.place
import models.review


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
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file at the path __file_path"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            dic = FileStorage.__objects.copy()
            # print(f"prev obj={FileStorage.__objects}")
            for k in dic:
                dic[k] = dic[k].to_dict()
            # print(f"post obj={FileStorage.__objects}")
            # print(f"post dic={dic}")
            file.write(dumps(dic))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding='utf-8') as file:
                dic = loads(file.read())
                for key, val in dic.items():
                    ob = dic[key]['__class__']
                    ob1 = "models." + {
                        'BaseModel': 'base_model',
                        'User': 'user',
                        'State': 'state',
                        'City': 'city',
                        'Place': 'place',
                        'Amenity': 'amenity',
                        'Review': 'review'}[ob]
                    FileStorage.__objects[key] = eval(
                        ob1 + f".{ob}" + "(**val)")
