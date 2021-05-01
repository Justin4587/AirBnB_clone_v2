#!/usr/bin/python3
"""
module for db class storage
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.base_model import Base
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """db storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """create engine"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        env = getenv("HBNB_ENV", "none")
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """shows all objects of given type"""
        result = {}
        if cls is not None:
            objs = self.__session.query(eval(cls)).all()
            for i in objs:
                k = i.__class__.__name__ + "." + i.id
                result[k] = i
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for i in objs:
                            key = i.__class__.__name__ + "." + i.id
                            result[key] = i
        return result

    def new(self, obj):
        """adds object to current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes object from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates tables and current database"""
        self.__session = Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        """ close """
        self.__session.remove()
