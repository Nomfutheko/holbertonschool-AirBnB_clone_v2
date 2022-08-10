#!/usr/bin/Python3
"""This module defines the engine for the MySQL database"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')
env = os.getenv('HBNB_ENV')


class DBStorage:
    """Defining the class DBStorage"""

    __classes = [State, City, User, Place, Review, Amenity]
    __engine = None
    __session = None

    def __init__(self):
        """Contructor for the class DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
    if env == "test":
        Base.MetaData.drop_all()

    def all(self, cls=None):
        """Method to return a dictionary of objects"""
        my_dict = {}
        if cls in self.__classes:
            result = DBStorage.__session.query(cls)
            for row in result:
                key = "{}.{}".format(row.__class__.__name__, row.id)
                my_dict[key] = row
        elif cls is None:
            for cl in self.__classes:
                result = DBStorage.__session.query(cl)
                for row in result:
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    my_dict[key] = row
        return my_dict

