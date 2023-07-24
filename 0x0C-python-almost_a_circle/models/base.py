#!/usr/bin/python3
"""Base class module"""
import json
import csv
import os
import turtle


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """static method returns the JSON string of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string represented by json_string"""
        if json_string is None:
            return []
        list_dict = json.loads(json_string)
        return list_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON rep of list_objs to file"""
        if list_objs is None:
            temp = []
        else:
            temp = [obj.to_dictionary() for obj in list_objs]
        with open(f'{cls.__name__}.json', 'w') as f:
            temp_str = Base.to_json_string(temp)
            f.write(temp_str)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        args = []
        dummy_obj = Base.__init_dummy(cls, *args)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """loads instance from file"""
        try:
            with open(f'{cls.__name__}.json', 'r') as f:
                # json_str = Base.from_json_string(f.read())
                list_dict_obj = Base.from_json_string(f.read())
            return [cls.create(**obj_dict) for obj_dict in list_dict_obj]
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a graphic window and draws all the rectangles and squares"""
        pet = turtle.getturtle()
        for shape in list_rectangles + list_squares:
            pet.penup()
            pet.setpos(shape.x, shape.y)
            pet.pendown()
            pet.forward(shape.width)
            pet.right(90)
            pet.forward(shape.height)
            pet.right(90)
            pet.forward(shape.width)
            pet.right(90)
            pet.forward(shape.height)
            pet.setheading(0)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes instance to csv format"""
        list_obj_vals = [obj.to_dictionary().values()
                         for obj in list_objs if type(obj) is cls]
        with open(f'{cls.__name__}.csv', 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(list_obj_vals)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes csv to instance"""
        args = []
        if not os.path.exists(f'{cls.__name__}.csv'):
            return args
        dummy = Base.__init_dummy(cls, *args)
        with open(f'{cls.__name__}.csv', 'r') as f:
            # read file
            csv_format_str = f.read()
        # split the string to a list of strings - delim: newline character '\n'
        csv_str_list = csv_format_str.split('\n')[:-1]
        # split each string to a list of obj values - delim: comma ','
        csv_val_list = [[int(x) for x in val_list.split(',')]
                        for val_list in csv_str_list]
        # create dict representations of each instance from the csv_val_list
        obj_dict_list = [dict(zip(dummy.to_dictionary().keys(), vals))
                         for vals in csv_val_list]
        # create instance from each dict representation
        args = [cls.create(**val_dict) for val_dict in obj_dict_list]
        return args

    def __init_dummy(cls, *args):
        """private utility method"""
        list_args = list(args)
        list_args.append(1)
        try:
            obj = cls(*list_args)
            return obj
        except TypeError:
            return Base.__init_dummy(cls, *list_args)
