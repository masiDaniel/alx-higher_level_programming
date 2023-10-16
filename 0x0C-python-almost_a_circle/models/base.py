#!/usr/bin/python3
"""module"""
import json


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json rep of list_dictionaries"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes  JSON string rep of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as F:
            if list_objs is None:
                F.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                F.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_data = cls(1, 1)
        else:
            dummy_data = cls(1)
        dummy_data.update(**dictionary)
        return dummy_data

    @classmethod
    def load_from_file(cls):
        """ a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**obj) for obj in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the list of objects to a csv file"""
        import csv
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
                return filename
            return None

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from csv file"""
        import csv
        filename = cls.__name__ + ".csv"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                return [cls.create(**{k: int(v) for k, v in
                                      obj.items()})
                        for obj in reader]
        else:
            return []
