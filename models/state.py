
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") != "db":
        name = ""

        @property
        def cities(self):
            """List of cities in that state"""
            result = []
            for i in models.storage.all("City").values():
                if i.state_id == self.id:
                    result.append(city)
            return result
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
